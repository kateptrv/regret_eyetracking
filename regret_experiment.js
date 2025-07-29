/************************** 
 * Regret_Experiment *
 **************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'regret_experiment';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const instructionsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(instructionsLoopBegin(instructionsLoopScheduler));
flowScheduler.add(instructionsLoopScheduler);
flowScheduler.add(instructionsLoopEnd);


const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);






flowScheduler.add(EndScreenRoutineBegin());
flowScheduler.add(EndScreenRoutineEachFrame());
flowScheduler.add(EndScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'instructions.xlsx', 'path': 'instructions.xlsx'},
    {'name': 'images/tree-1.png', 'path': 'images/tree-1.png'},
    {'name': 'images/tree-2.png', 'path': 'images/tree-2.png'},
    {'name': 'images/tree-3.png', 'path': 'images/tree-3.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  // Run 'Begin Experiment' code from init_vars
  import * as random from 'random';
  participant_cond = Math.random.choice([0, 1]);
  PROBS = [0.2, 0.5, 0.7];
  Math.random.shuffle(PROBS);
  [prob_left, prob_up, prob_right] = PROBS;
  trial_num = 0;
  points = 0;
  expInfo["participant_cond"] = participant_cond;
  expInfo["prob_left"] = prob_left;
  expInfo["prob_up"] = prob_up;
  expInfo["prob_right"] = prob_right;
  
  // Initialize components for Routine "Fixation"
  FixationClock = new util.Clock();
  fixcross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixcross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Choice"
  ChoiceClock = new util.Clock();
  tree1_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tree1_img', units : 'pix', 
    image : 'images/tree-1.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 300), 0], 
    draggable: false,
    size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  tree2_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tree2_img', units : 'pix', 
    image : 'images/tree-2.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  tree3_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tree3_img', units : 'pix', 
    image : 'images/tree-3.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [300, 0], 
    draggable: false,
    size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  key_resp_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Feedback"
  FeedbackClock = new util.Clock();
  appleImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'appleImage', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "RegretRating"
  RegretRatingClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'How much do you regret this choice? Press a number key from 1-0, with 0 representing 10.\n\n1                      5                   0(10)       \n<---------------------------------------------->\nNot                                         Very\nvery                                        Much\nmuch',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  regret_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from regretlogic
  skip_regret = false;
  
  // Initialize components for Routine "ITI"
  ITIClock = new util.Clock();
  blank_screen = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank_screen',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "EndScreen"
  EndScreenClock = new util.Clock();
  // Run 'Begin Experiment' code from end_experiment
  import * as np from 'numpy';
  regret_ratings = function () {
      var _pj_a = [], _pj_b = trials.data["regret_rating"];
      for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
          var r = _pj_b[_pj_c];
          if ((r !== "NA")) {
              _pj_a.push(r);
          }
      }
      return _pj_a;
  }
  .call(this);
  if (regret_ratings) {
      avg_regret = util.round(np.mean(regret_ratings), 2);
  } else {
      avg_regret = "N/A";
  }
  total_points = util.sum(trials.data["points"]);
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function instructionsLoopBegin(instructionsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    instructions = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 5, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'instructions.xlsx',
      seed: undefined, name: 'instructions'
    });
    psychoJS.experiment.addLoop(instructions); // add the loop to the experiment
    currentLoop = instructions;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisInstruction of instructions) {
      snapshot = instructions.getSnapshot();
      instructionsLoopScheduler.add(importConditions(snapshot));
      instructionsLoopScheduler.add(InstructionsRoutineBegin(snapshot));
      instructionsLoopScheduler.add(InstructionsRoutineEachFrame());
      instructionsLoopScheduler.add(InstructionsRoutineEnd(snapshot));
      instructionsLoopScheduler.add(instructionsLoopEndIteration(instructionsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function instructionsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(instructions);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function instructionsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 10, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(FixationRoutineBegin(snapshot));
      trialsLoopScheduler.add(FixationRoutineEachFrame());
      trialsLoopScheduler.add(FixationRoutineEnd(snapshot));
      trialsLoopScheduler.add(ChoiceRoutineBegin(snapshot));
      trialsLoopScheduler.add(ChoiceRoutineEachFrame());
      trialsLoopScheduler.add(ChoiceRoutineEnd(snapshot));
      trialsLoopScheduler.add(FeedbackRoutineBegin(snapshot));
      trialsLoopScheduler.add(FeedbackRoutineEachFrame());
      trialsLoopScheduler.add(FeedbackRoutineEnd(snapshot));
      trialsLoopScheduler.add(RegretRatingRoutineBegin(snapshot));
      trialsLoopScheduler.add(RegretRatingRoutineEachFrame());
      trialsLoopScheduler.add(RegretRatingRoutineEnd(snapshot));
      trialsLoopScheduler.add(ITIRoutineBegin(snapshot));
      trialsLoopScheduler.add(ITIRoutineEachFrame());
      trialsLoopScheduler.add(ITIRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    InstructionsClock.reset();
    routineTimer.reset();
    InstructionsMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('Instructions.started', globalClock.getTime());
    InstructionsMaxDuration = null
    // keep track of which components have finished
    InstructionsComponents = [];
    
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function InstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions' ---
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function InstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions' ---
    for (const thisComponent of InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Instructions.stopped', globalClock.getTime());
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function FixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Fixation' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    FixationClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    FixationMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('Fixation.started', globalClock.getTime());
    FixationMaxDuration = null
    // keep track of which components have finished
    FixationComponents = [];
    FixationComponents.push(fixcross);
    
    for (const thisComponent of FixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function FixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Fixation' ---
    // get current time
    t = FixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixcross* updates
    if (t >= 0.0 && fixcross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixcross.tStart = t;  // (not accounting for frame time here)
      fixcross.frameNStart = frameN;  // exact frame index
      
      fixcross.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fixcross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixcross.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function FixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Fixation' ---
    for (const thisComponent of FixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Fixation.stopped', globalClock.getTime());
    if (FixationMaxDurationReached) {
        FixationClock.add(FixationMaxDuration);
    } else {
        FixationClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function ChoiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Choice' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    ChoiceClock.reset();
    routineTimer.reset();
    ChoiceMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_1.keys = undefined;
    key_resp_1.rt = undefined;
    _key_resp_1_allKeys = [];
    // Run 'Begin Routine' code from choice_logic
    trial_num += 1;
    psychoJS.experiment.addData("trial_num", trial_num);
    psychoJS.experiment.addData("participant_cond", participant_cond);
    psychoJS.experiment.addData("prob_left", prob_left);
    psychoJS.experiment.addData("prob_up", prob_up);
    psychoJS.experiment.addData("prob_right", prob_right);
    
    psychoJS.experiment.addData('Choice.started', globalClock.getTime());
    ChoiceMaxDuration = null
    // keep track of which components have finished
    ChoiceComponents = [];
    ChoiceComponents.push(tree1_img);
    ChoiceComponents.push(tree2_img);
    ChoiceComponents.push(tree3_img);
    ChoiceComponents.push(key_resp_1);
    
    for (const thisComponent of ChoiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function ChoiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Choice' ---
    // get current time
    t = ChoiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *tree1_img* updates
    if (t >= 0.0 && tree1_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tree1_img.tStart = t;  // (not accounting for frame time here)
      tree1_img.frameNStart = frameN;  // exact frame index
      
      tree1_img.setAutoDraw(true);
    }
    
    
    // *tree2_img* updates
    if (t >= 0.0 && tree2_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tree2_img.tStart = t;  // (not accounting for frame time here)
      tree2_img.frameNStart = frameN;  // exact frame index
      
      tree2_img.setAutoDraw(true);
    }
    
    
    // *tree3_img* updates
    if (t >= 0.0 && tree3_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tree3_img.tStart = t;  // (not accounting for frame time here)
      tree3_img.frameNStart = frameN;  // exact frame index
      
      tree3_img.setAutoDraw(true);
    }
    
    
    // *key_resp_1* updates
    if (t >= 0.0 && key_resp_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_1.tStart = t;  // (not accounting for frame time here)
      key_resp_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_1.clearEvents(); });
    }
    
    if (key_resp_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_1.getKeys({keyList: ['left', 'right', 'up'], waitRelease: false});
      _key_resp_1_allKeys = _key_resp_1_allKeys.concat(theseKeys);
      if (_key_resp_1_allKeys.length > 0) {
        key_resp_1.keys = _key_resp_1_allKeys[_key_resp_1_allKeys.length - 1].name;  // just the last key pressed
        key_resp_1.rt = _key_resp_1_allKeys[_key_resp_1_allKeys.length - 1].rt;
        key_resp_1.duration = _key_resp_1_allKeys[_key_resp_1_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ChoiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function ChoiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Choice' ---
    for (const thisComponent of ChoiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Choice.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_1.corr, level);
    }
    psychoJS.experiment.addData('key_resp_1.keys', key_resp_1.keys);
    if (typeof key_resp_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_1.rt', key_resp_1.rt);
        psychoJS.experiment.addData('key_resp_1.duration', key_resp_1.duration);
        routineTimer.reset();
        }
    
    key_resp_1.stop();
    // Run 'End Routine' code from choice_logic
    psychoJS.experiment.addData("trial_num", trial_num);
    psychoJS.experiment.addData("participant_cond", participant_cond);
    choice_key = key_resp_1.keys;
    choice_rt = key_resp_1.rt;
    psychoJS.experiment.addData("choice_key", choice_key);
    psychoJS.experiment.addData("choice_rt", choice_rt);
    
    // the Routine "Choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function FeedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Feedback' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    FeedbackClock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    FeedbackMaxDurationReached = false;
    // update component parameters for each repeat
    appleImage.setImage(apple_img);
    psychoJS.experiment.addData('Feedback.started', globalClock.getTime());
    FeedbackMaxDuration = null
    // keep track of which components have finished
    FeedbackComponents = [];
    FeedbackComponents.push(appleImage);
    
    for (const thisComponent of FeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function FeedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Feedback' ---
    // get current time
    t = FeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *appleImage* updates
    if (t >= 0.0 && appleImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      appleImage.tStart = t;  // (not accounting for frame time here)
      appleImage.frameNStart = frameN;  // exact frame index
      
      appleImage.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (appleImage.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      appleImage.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function FeedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Feedback' ---
    for (const thisComponent of FeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Feedback.stopped', globalClock.getTime());
    if (FeedbackMaxDurationReached) {
        FeedbackClock.add(FeedbackMaxDuration);
    } else {
        FeedbackClock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function RegretRatingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RegretRating' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    RegretRatingClock.reset();
    routineTimer.reset();
    RegretRatingMaxDurationReached = false;
    // update component parameters for each repeat
    regret_key.keys = undefined;
    regret_key.rt = undefined;
    _regret_key_allKeys = [];
    // Run 'Begin Routine' code from regretlogic
    skip_regret = (! (((participant_cond === 1) && (trial_num <= 30)) && (points === 0)));
    if (skip_regret) {
        continueRoutine = false;
        psychoJS.experiment.addData("regret_rating", "NA");
        psychoJS.experiment.addData("regret_rt", "NA");
    }
    
    psychoJS.experiment.addData('RegretRating.started', globalClock.getTime());
    RegretRatingMaxDuration = null
    // keep track of which components have finished
    RegretRatingComponents = [];
    RegretRatingComponents.push(text);
    RegretRatingComponents.push(regret_key);
    
    for (const thisComponent of RegretRatingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function RegretRatingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RegretRating' ---
    // get current time
    t = RegretRatingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // *regret_key* updates
    if (t >= 0.0 && regret_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      regret_key.tStart = t;  // (not accounting for frame time here)
      regret_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { regret_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { regret_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { regret_key.clearEvents(); });
    }
    
    if (regret_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = regret_key.getKeys({keyList: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], waitRelease: false});
      _regret_key_allKeys = _regret_key_allKeys.concat(theseKeys);
      if (_regret_key_allKeys.length > 0) {
        regret_key.keys = _regret_key_allKeys[_regret_key_allKeys.length - 1].name;  // just the last key pressed
        regret_key.rt = _regret_key_allKeys[_regret_key_allKeys.length - 1].rt;
        regret_key.duration = _regret_key_allKeys[_regret_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RegretRatingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function RegretRatingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RegretRating' ---
    for (const thisComponent of RegretRatingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('RegretRating.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(regret_key.corr, level);
    }
    psychoJS.experiment.addData('regret_key.keys', regret_key.keys);
    if (typeof regret_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('regret_key.rt', regret_key.rt);
        psychoJS.experiment.addData('regret_key.duration', regret_key.duration);
        routineTimer.reset();
        }
    
    regret_key.stop();
    // Run 'End Routine' code from regretlogic
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if ((! skip_regret)) {
        k = regret_key.keys;
        if (_pj.in_es6(k, [null, ""])) {
            rating = "NA";
        } else {
            if ((k === "0")) {
                rating = 10;
            } else {
                rating = Number.parseInt(k);
            }
        }
        psychoJS.experiment.addData("regret_rating", rating);
        psychoJS.experiment.addData("regret_rt", regret_key.rt);
    }
    
    // the Routine "RegretRating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function ITIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ITI' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    ITIClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    ITIMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('ITI.started', globalClock.getTime());
    ITIMaxDuration = null
    // keep track of which components have finished
    ITIComponents = [];
    ITIComponents.push(blank_screen);
    
    for (const thisComponent of ITIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function ITIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ITI' ---
    // get current time
    t = ITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blank_screen* updates
    if (t >= 0.0 && blank_screen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blank_screen.tStart = t;  // (not accounting for frame time here)
      blank_screen.frameNStart = frameN;  // exact frame index
      
      blank_screen.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (blank_screen.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blank_screen.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ITIComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function ITIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ITI' ---
    for (const thisComponent of ITIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ITI.stopped', globalClock.getTime());
    if (ITIMaxDurationReached) {
        ITIClock.add(ITIMaxDuration);
    } else {
        ITIClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function EndScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EndScreen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    EndScreenClock.reset();
    routineTimer.reset();
    EndScreenMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('EndScreen.started', globalClock.getTime());
    EndScreenMaxDuration = null
    // keep track of which components have finished
    EndScreenComponents = [];
    
    for (const thisComponent of EndScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function EndScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EndScreen' ---
    // get current time
    t = EndScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function EndScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EndScreen' ---
    for (const thisComponent of EndScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('EndScreen.stopped', globalClock.getTime());
    // the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
