# ALWAYS MAKE SURE .VENV IS ACTIVATED AND SET TO PYTHON 3.10 BEFORE RUNNING ANYTHING
# make sure to use Python 3.10; pip install psychopy, pylink
# make sure current directory is set to regret_eyetracking 
# the current code is a minimal example; eyetracking parts are commented out because they won't work without the full setup
# need to figure out what to do about the regret slider--having a mouse cursor is not ideal since we have eye tracking; the slider is clunky as is. maybe a 1-10 scale could work
# also for now the condition is being set manually; in the future will randomize
# also don't need condition 2, this is just a leftover from the old version of the experiment

from psychopy import visual, core, event, gui, data, logging
#import pylink
#from pylink import EyeLink, openGraphicsEx
import random
import os

# === Setup experiment info ===
exp_info = {"Participant": "", "Condition (1-4)": 2}
dlg = gui.DlgFromDict(dictionary=exp_info)
if not dlg.OK:
    core.quit()

if not os.path.exists("data"):
    os.makedirs("data")

filename = f"data/{exp_info['Participant']}_fruit"
condition = int(exp_info["Condition (1-4)"])
thisExp = data.ExperimentHandler(dataFileName=filename)

# === Setup Eyelink ===
# tracker = EyeLink()
# openGraphicsEx(pylink.getEYELINK().graphics)
# tracker.openDataFile('test.edf')
# tracker.sendCommand("file_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON")
# tracker.sendCommand("file_sample_data = LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS")

# === Setup window ===
win = visual.Window([1280, 800], color='white', units='pix', fullscr=False)
win.mouseVisible = False

# === Stimuli ===
tree_files = ['images/tree-1.png', 'images/tree-2.png', 'images/tree-3.png']
fruit_files = {'ripe': 'images/apple-high.png', 'rotten': 'images/apple-neg.png'}
tree_stims = [visual.ImageStim(win, image=f, size=(200, 300), pos=(-300 + i*300, 0)) for i, f in enumerate(tree_files)]
fruit_stim = visual.ImageStim(win, size=(150, 150), pos=(0, 0))
text = visual.TextStim(win, text='', color='black', height=32, wrapWidth=1000)
slider = visual.Slider(
    win=win,
    units='pix',           # same units as the window
    size=(800, 40),        # 800 px wide, 40 px tall
    pos=(0, -200),         # ~¼ of the way down the screen
    ticks=(0, 25, 50, 75, 100),
    labels=["Not at all", "", "", "", "Very much"],
    granularity=1,
    style='rating',        # gives the classic “line with a handle”
    color='black',         # track colour
    fillColor='black',     # handle fill
    borderColor='black'    # handle border
)

# === Instructions ===
instruction_files = [
    'images/instructions01.png', 'images/instructions02.png', 'images/instructions03.png',
    'images/instructionsBonus.png', 'images/instructions04.png',
    'images/instructions05.png', 'images/instructions06.png'
]
instruction_files += {
    1: ['images/instructions08.png'],
    2: ['images/instructions072.png'],
    3: ['images/instructions073.png'],
    4: ['images/instructions074.png']
}[condition]

for img in instruction_files:
    inst = visual.ImageStim(win, image=img, size=(900, 600))
    inst.draw()
    win.flip()
    event.waitKeys(keyList=['space'])


# === Begin Experiment Instruction ===
text.text = "Press space to begin the experiment."
text.draw()
win.flip()
event.waitKeys(keyList=['space'])

# === Experiment variables ===
tree_probs = [[0.7, 0.3], [0.2, 0.8], [0.5, 0.5]]
random.shuffle(tree_probs)  
total_points = 0
trial_counter = 0
total_multiple_choice_trials = 0
max_trials = 60

# === Start Eyelink recording ===
# tracker.setOfflineMode()
# core.wait(0.1)
# tracker.startRecording(1, 1, 1, 1)

# === Trial loop ===
for i in range(max_trials):
    trial_counter += 1

    for t in tree_stims:
        t.draw()
    win.flip()
    # tracker.sendMessage(f"TRIAL_{i+1}_START")

    keys = event.waitKeys(keyList=['left', 'up', 'right', 'escape'])
    if 'escape' in keys:
        break
    choice = {'left': 0, 'up': 1, 'right': 2}[keys[0]]
    chosen_prob = tree_probs[choice][0]
    outcome = 'ripe' if random.random() < chosen_prob else 'rotten'
    points = 1 if outcome == 'ripe' else 0
    total_points += points

    # Show fruit
    fruit_stim.image = fruit_files[outcome]
    fruit_stim.pos = (-300 + choice * 300, 100)
    fruit_stim.draw()
    win.flip()
    # tracker.sendMessage(f"CHOICE_{choice}_OUTCOME_{outcome}")
    core.wait(0.5)

    # Conditional regret
    show_slider = False
    if condition == 2 and points == 0:
        show_slider = True
    elif condition == 3 and points == 0 and i < 30:
        show_slider = True
    elif condition == 4 and points == 0 and i >= 30:
        show_slider = True

    # -------------- REGRET RATING  (keyboard only) --------------
    if show_slider:
        win.mouseVisible = False          # keep cursor hidden

        slider.reset()
        n_ticks = len(slider.ticks)

        current_idx = n_ticks // 2       
        slider.markerPos = (current_idx - (n_ticks-1)/2) / ((n_ticks-1)/2)

        text.text = (
            "How much do you regret this choice?\n"
            "← / →  to move   •   Space / Enter  to confirm"
        )

        rating_done = False
        start_time  = core.getTime()      

        while not rating_done:
            text.draw()
            slider.draw()
            win.flip()

            for key in event.getKeys():
                if key == "left" and current_idx > 0:
                    current_idx -= 1
                elif key == "right" and current_idx < n_ticks - 1:
                    current_idx += 1
                elif key in ("space", "return", "enter"):
                    slider.rating = slider.ticks[current_idx]
                    slider.rt = core.getTime() - start_time
                    rating_done = True

                slider.markerPos = (current_idx - (n_ticks-1)/2) / ((n_ticks-1)/2)

        thisExp.addData('regret_rating', slider.rating)
    else:
        thisExp.addData('regret_rating', 'NA')
    # -------------------------------------------------------------

    thisExp.addData('trial', i+1)
    thisExp.addData('choice', choice)
    thisExp.addData('outcome', outcome)
    thisExp.addData('points', points)
    thisExp.addData('total_points', total_points)
    thisExp.addData('condition', condition)
    thisExp.nextEntry()

    # Mid-point break
    if i == 29 and condition in [3, 4]:
        text.text = "Part 1 complete. Press space to continue."
        text.draw()
        win.flip()
        event.waitKeys(keyList=['space'])

# === Stop Eyelink ===
# tracker.stopRecording()
# core.wait(0.1)
# tracker.setOfflineMode()
# tracker.closeDataFile()
# edf_name = f"{exp_info['Participant']}.edf"
# tracker.receiveDataFile('test.edf', edf_name)
# tracker.close()

# === Save and exit ===
thisExp.saveAsWideText(f"{filename}.csv")
text.text = "Thank you for participating!\n\nTotal Points: {}".format(total_points)
text.draw()
win.flip()
core.wait(3)
win.close()
core.quit()