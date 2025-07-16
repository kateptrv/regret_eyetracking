"""
regret_experiment.py
Run locally in the PsychoPy desktop app (no Pavlovia needed).

Folder layout
├─ regret_experiment.py            ← THIS FILE
├─ instructions.xlsx               ← 1 col named 'image' (paths to instruction PNGs)
├─ conditions.xlsx                 ← per-trial variables (see below)
├─ images/
│   instructions01.png  tree-1.png  tree-2.png  tree-3.png  default.png  …
└─ data/   (created automatically)
"""

from psychopy import core, visual, event, data, gui, logging
from pathlib import Path
import numpy as np

# ------------------------ 1  EXPERIMENT INFO DIALOG --------------------------
expName = "regret_experiment"
expInfo = {"participant": ""}
dlg = gui.DlgFromDict(expInfo, title=expName)
if not dlg.OK:
    core.quit()

# ------------------------ 2  WINDOW & BASIC STIMULI --------------------------
win = visual.Window(
    size=[1280, 720],
    fullscr=True,
    units="height",
    color="black"
)
fixcross = visual.TextStim(win, text="+", height=0.05)
blank_txt = visual.TextStim(win, text="")

# tree positions (L-C-R)
tree_positions = [(-0.5, 0), (0.0, 0), (0.5, 0)]
tree_files = [f"images/tree-{i}.png" for i in (1, 2, 3)]
trees = [
    visual.ImageStim(win, image=f, pos=p, size=(0.35, 0.35))
    for f, p in zip(tree_files, tree_positions)
]

# feedback apple (image & position will be updated each trial)
apple = visual.ImageStim(win, image="images/apple-high.png", size=(0.28, 0.28))

rating_prompt = visual.TextStim(
    win,
    text=(
        "How much do you regret this choice?\n"
        "Press 1 – 0  (0 = 10)\n\n"
        "1                        5                       0(10)\n"
        "<------------------------------------------------->\n"
        "Not very much                          Very much"
    ),
    height=0.045,
    wrapWidth=1.2,
)

end_msg = visual.TextStim(win, height=0.06)

# ------------------------ 3  HANDY FUNCTIONS ---------------------------------
def flush():
    """Clear keybuffer and flip once (black screen)."""
    event.clearEvents()
    win.flip()

def show(stim, dur=None, keyList=None):
    """Draw *stim* until duration expires or a key in keyList is pressed."""
    timer = core.Clock()
    flush()
    while True:
        stim.draw()
        win.flip()
        if keyList:
            keys = event.getKeys(keyList=keyList)
            if keys:
                return keys[0], timer.getTime()
        if dur is not None and timer.getTime() >= dur:
            return None, timer.getTime()

def safe_quit():
    if "escape" in event.getKeys():
        win.close(); core.quit()

# ------------------------ 4  INSTRUCTIONS LOOP --------------------------------
instr_trials = data.TrialHandler(
    nReps=1,
    method="random",
    trialList=data.importConditions("instructions.xlsx"),
    name="instructions"
)

for instr in instr_trials:
    img = visual.ImageStim(win, image=instr["image"])
    show(img, keyList=["space"])  # space to advance
    safe_quit()

# ------------------------ 5  MAIN TRIAL LOOP ---------------------------------
trials = data.TrialHandler(
    nReps=1,
    method="sequential",
    trialList=data.importConditions("conditions.xlsx"),
    name="trials"
)

total_points = 0
regret_ratings = []

for trial in trials:
    # 5.1 Fixation ----------------------------------------------------------------
    show(fixcross, dur=1.0)
    safe_quit()

    # 5.2 Choice -------------------------------------------------------------------
    for t in trees:
        t.draw()
    win.flip()

    key, rt = show(blank_txt, keyList=["left", "up", "right", "escape"])
    if key == "escape":
        safe_quit()
    choice_idx = {"left": 0, "up": 1, "right": 2}[key]

    # store choice
    trials.addData("choice_key", key)
    trials.addData("choice_rt", rt)
    trials.addData("choice_idx", choice_idx)

    # 5.3 Determine outcome & feedback --------------------------------------------
    # Spreadsheet should contain at least:
    #  - 'apple_img' (image path)
    #  - 'apple_x', 'apple_y'  (floats, pos in height units)
    #  - 'points'  (numeric reward)
    img_file = trial.get("apple_img", "images/apple-high.png")
    apple.image = img_file
    apple.pos = (trial.get("apple_x", 0.0), trial.get("apple_y", -0.2))
    points = trial.get("points", 0)
    total_points += points

    trials.addData("points", points)
    trials.addData("apple_img_shown", img_file)

    show(apple, dur=1.0)
    safe_quit()

    # 5.4 Regret rating ------------------------------------------------------------
    key, _ = show(rating_prompt, keyList=list("1234567890"))
    rating_val = 10 if key == "0" else int(key)
    regret_ratings.append(rating_val)
    trials.addData("regret_rating", rating_val)

    # 5.5 ITI ----------------------------------------------------------------------
    show(blank_txt, dur=1.0)
    safe_quit()

# ------------------------ 6  END-OF-EXPERIMENT SCREEN -------------------------
avg_regret = np.mean(regret_ratings) if regret_ratings else np.nan
end_msg.text = (
    f"Experiment complete!\n\n"
    f"Total points : {total_points}\n"
    f"Average regret : {avg_regret:.2f}\n\n"
    f"Press any key to exit."
)
show(end_msg, keyList=None)
event.waitKeys()

# ------------------------ 7  SAVE & QUIT --------------------------------------
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
outfile = data_dir / f"{expInfo['participant']}_{expName}.csv"
trials.saveAsWideText(outfile, delim=",")
logging.flush()

win.close()
core.quit()