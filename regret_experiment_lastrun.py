﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Wed Jul 16 15:25:50 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_feedback
apple_pos = (0, 0)
apple_img = 'images/apple-neg.png'
points = 0
tree_prob = 0.0
import random
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'regret_experiment'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1440, 900]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/katepetrova/Library/CloudStorage/GoogleDrive-kpetrova@stanford.edu/Shared drives/SPL_Kate Petrova/regret_eyetracking/regret_eyetracking/regret_experiment_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp_1') is None:
        # initialise key_resp_1
        key_resp_1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_1',
        )
    if deviceManager.getDevice('regret_key') is None:
        # initialise regret_key
        regret_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='regret_key',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Instructions" ---
    # Run 'Begin Experiment' code from init_vars
    import random
    
    # -------------------
    # Participant-level settings
    # -------------------
    # 0 = No-Regret, 1 = Regret-First-30
    participant_cond = random.choice([0, 1])
    
    # Randomize prob assignment to LEFT / UP / RIGHT once for this participant
    PROBS = [0.2, 0.5, 0.7]
    random.shuffle(PROBS)
    prob_left, prob_up, prob_right = PROBS
    
    # State vars
    trial_num = 0      # increments each main trial
    points = 0         # outcome from last trial
    
    # Put mapping in expInfo so it is saved with the data file header
    expInfo['participant_cond'] = participant_cond
    expInfo['prob_left']  = prob_left
    expInfo['prob_up']    = prob_up
    expInfo['prob_right'] = prob_right
    
    # --- Initialize components for Routine "Fixation" ---
    fixcross = visual.TextStim(win=win, name='fixcross',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Choice" ---
    tree1_img = visual.ImageStim(
        win=win,
        name='tree1_img', units='pix', 
        image='images/tree-1.png', mask=None, anchor='center',
        ori=0.0, pos=(-300, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    tree2_img = visual.ImageStim(
        win=win,
        name='tree2_img', units='pix', 
        image='images/tree-2.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    tree3_img = visual.ImageStim(
        win=win,
        name='tree3_img', units='pix', 
        image='images/tree-3.png', mask=None, anchor='center',
        ori=0.0, pos=(300, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    key_resp_1 = keyboard.Keyboard(deviceName='key_resp_1')
    
    # --- Initialize components for Routine "Feedback" ---
    appleImage = visual.ImageStim(
        win=win,
        name='appleImage', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "RegretRating" ---
    text = visual.TextStim(win=win, name='text',
        text='How much do you regret this choice? Press a number key from 1-0, with 0 representing 10.\n\n1                      5                   0(10)       \n<---------------------------------------------->\nNot                                         Very\nvery                                        Much\nmuch',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    regret_key = keyboard.Keyboard(deviceName='regret_key')
    # Run 'Begin Experiment' code from regretlogic
    skip_regret = False
    
    # --- Initialize components for Routine "ITI" ---
    blank_screen = visual.TextStim(win=win, name='blank_screen',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "EndScreen" ---
    # Run 'Begin Experiment' code from end_experiment
    
    
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # set up handler to look after randomisation of conditions etc
    instructions = data.TrialHandler2(
        name='instructions',
        nReps=5.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('instructions.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(instructions)  # add the loop to the experiment
    thisInstruction = instructions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
    if thisInstruction != None:
        for paramName in thisInstruction:
            globals()[paramName] = thisInstruction[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisInstruction in instructions:
        currentLoop = instructions
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
        if thisInstruction != None:
            for paramName in thisInstruction:
                globals()[paramName] = thisInstruction[paramName]
        
        # --- Prepare to start Routine "Instructions" ---
        # create an object to store info about Routine Instructions
        Instructions = data.Routine(
            name='Instructions',
            components=[],
        )
        Instructions.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Instructions
        Instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Instructions.tStart = globalClock.getTime(format='float')
        Instructions.status = STARTED
        thisExp.addData('Instructions.started', Instructions.tStart)
        Instructions.maxDuration = None
        # keep track of which components have finished
        InstructionsComponents = Instructions.components
        for thisComponent in Instructions.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Instructions" ---
        # if trial has changed, end Routine now
        if isinstance(instructions, data.TrialHandler2) and thisInstruction.thisN != instructions.thisTrial.thisN:
            continueRoutine = False
        Instructions.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Instructions.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instructions.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Instructions" ---
        for thisComponent in Instructions.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Instructions
        Instructions.tStop = globalClock.getTime(format='float')
        Instructions.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Instructions.stopped', Instructions.tStop)
        # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 5.0 repeats of 'instructions'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=10.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "Fixation" ---
        # create an object to store info about Routine Fixation
        Fixation = data.Routine(
            name='Fixation',
            components=[fixcross],
        )
        Fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Fixation
        Fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Fixation.tStart = globalClock.getTime(format='float')
        Fixation.status = STARTED
        thisExp.addData('Fixation.started', Fixation.tStart)
        Fixation.maxDuration = None
        # keep track of which components have finished
        FixationComponents = Fixation.components
        for thisComponent in Fixation.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Fixation" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        Fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixcross* updates
            
            # if fixcross is starting this frame...
            if fixcross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixcross.frameNStart = frameN  # exact frame index
                fixcross.tStart = t  # local t and not account for scr refresh
                fixcross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixcross.started')
                # update status
                fixcross.status = STARTED
                fixcross.setAutoDraw(True)
            
            # if fixcross is active this frame...
            if fixcross.status == STARTED:
                # update params
                pass
            
            # if fixcross is stopping this frame...
            if fixcross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixcross.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixcross.tStop = t  # not accounting for scr refresh
                    fixcross.tStopRefresh = tThisFlipGlobal  # on global time
                    fixcross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixcross.stopped')
                    # update status
                    fixcross.status = FINISHED
                    fixcross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Fixation.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation" ---
        for thisComponent in Fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Fixation
        Fixation.tStop = globalClock.getTime(format='float')
        Fixation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Fixation.stopped', Fixation.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Fixation.maxDurationReached:
            routineTimer.addTime(-Fixation.maxDuration)
        elif Fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "Choice" ---
        # create an object to store info about Routine Choice
        Choice = data.Routine(
            name='Choice',
            components=[tree1_img, tree2_img, tree3_img, key_resp_1],
        )
        Choice.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_1
        key_resp_1.keys = []
        key_resp_1.rt = []
        _key_resp_1_allKeys = []
        # Run 'Begin Routine' code from choice_logic
        trial_num += 1
        thisExp.addData('trial_num', trial_num)
        
        # optional: log participant-level constants each trial
        thisExp.addData('participant_cond', participant_cond)
        thisExp.addData('prob_left', prob_left)
        thisExp.addData('prob_up', prob_up)
        thisExp.addData('prob_right', prob_right)
        # store start times for Choice
        Choice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Choice.tStart = globalClock.getTime(format='float')
        Choice.status = STARTED
        thisExp.addData('Choice.started', Choice.tStart)
        Choice.maxDuration = None
        # keep track of which components have finished
        ChoiceComponents = Choice.components
        for thisComponent in Choice.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Choice" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        Choice.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_img* updates
            
            # if tree1_img is starting this frame...
            if tree1_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tree1_img.frameNStart = frameN  # exact frame index
                tree1_img.tStart = t  # local t and not account for scr refresh
                tree1_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tree1_img.started')
                # update status
                tree1_img.status = STARTED
                tree1_img.setAutoDraw(True)
            
            # if tree1_img is active this frame...
            if tree1_img.status == STARTED:
                # update params
                pass
            
            # *tree2_img* updates
            
            # if tree2_img is starting this frame...
            if tree2_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tree2_img.frameNStart = frameN  # exact frame index
                tree2_img.tStart = t  # local t and not account for scr refresh
                tree2_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tree2_img.started')
                # update status
                tree2_img.status = STARTED
                tree2_img.setAutoDraw(True)
            
            # if tree2_img is active this frame...
            if tree2_img.status == STARTED:
                # update params
                pass
            
            # *tree3_img* updates
            
            # if tree3_img is starting this frame...
            if tree3_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tree3_img.frameNStart = frameN  # exact frame index
                tree3_img.tStart = t  # local t and not account for scr refresh
                tree3_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tree3_img.started')
                # update status
                tree3_img.status = STARTED
                tree3_img.setAutoDraw(True)
            
            # if tree3_img is active this frame...
            if tree3_img.status == STARTED:
                # update params
                pass
            
            # *key_resp_1* updates
            waitOnFlip = False
            
            # if key_resp_1 is starting this frame...
            if key_resp_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_1.frameNStart = frameN  # exact frame index
                key_resp_1.tStart = t  # local t and not account for scr refresh
                key_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_1.started')
                # update status
                key_resp_1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_1.getKeys(keyList=['left', 'right', 'up'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_1_allKeys.extend(theseKeys)
                if len(_key_resp_1_allKeys):
                    key_resp_1.keys = _key_resp_1_allKeys[-1].name  # just the last key pressed
                    key_resp_1.rt = _key_resp_1_allKeys[-1].rt
                    key_resp_1.duration = _key_resp_1_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Choice.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Choice.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Choice" ---
        for thisComponent in Choice.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Choice
        Choice.tStop = globalClock.getTime(format='float')
        Choice.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Choice.stopped', Choice.tStop)
        # check responses
        if key_resp_1.keys in ['', [], None]:  # No response was made
            key_resp_1.keys = None
        trials.addData('key_resp_1.keys',key_resp_1.keys)
        if key_resp_1.keys != None:  # we had a response
            trials.addData('key_resp_1.rt', key_resp_1.rt)
            trials.addData('key_resp_1.duration', key_resp_1.duration)
        # Run 'End Routine' code from choice_logic
        # Log decision
        thisExp.addData('trial_num', trial_num)
        thisExp.addData('participant_cond', participant_cond)
        
        # chosen key + RT
        choice_key = key_resp_1.keys
        choice_rt  = key_resp_1.rt
        thisExp.addData('choice_key', choice_key)
        thisExp.addData('choice_rt', choice_rt)
        
        # We'll fill in choice_prob & points in Feedback (after outcome known)
        # the Routine "Choice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Feedback" ---
        # create an object to store info about Routine Feedback
        Feedback = data.Routine(
            name='Feedback',
            components=[appleImage],
        )
        Feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_feedback
        # Which key was chosen on that trial?
        k = choice_key  # from Choice End Routine variable (defined above)
        # (if you prefer, use: k = getattr(key_resp_1, 'keys', None))
        
        # Map key to prob + apple position
        if k == 'left':
            apple_pos = (-300, 0)
            tree_prob = prob_left
        elif k == 'up':
            apple_pos = (0, 0)
            tree_prob = prob_up
        elif k == 'right':
            apple_pos = (300, 0)
            tree_prob = prob_right
        else:
            apple_pos = (0, 0)
            tree_prob = 0.0  # no response / unexpected key
        
        # Outcome
        if random.random() < float(tree_prob):
            apple_img = 'images/apple-high.png'
            points = 1
        else:
            apple_img = 'images/apple-neg.png'
            points = 0
        
        # Update display stim
        appleImage.setPos(apple_pos)
        appleImage.setImage(apple_img)
        
        # Log prob + outcome
        thisExp.addData('choice_prob', tree_prob)
        thisExp.addData('points', points)
        
        # Also helpful to repeat mapping (participant-level constants) each row
        thisExp.addData('prob_left', prob_left)
        thisExp.addData('prob_up', prob_up)
        thisExp.addData('prob_right', prob_right)
        appleImage.setImage(apple_img)
        # store start times for Feedback
        Feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Feedback.tStart = globalClock.getTime(format='float')
        Feedback.status = STARTED
        thisExp.addData('Feedback.started', Feedback.tStart)
        Feedback.maxDuration = None
        # keep track of which components have finished
        FeedbackComponents = Feedback.components
        for thisComponent in Feedback.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Feedback" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        Feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *appleImage* updates
            
            # if appleImage is starting this frame...
            if appleImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                appleImage.frameNStart = frameN  # exact frame index
                appleImage.tStart = t  # local t and not account for scr refresh
                appleImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(appleImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'appleImage.started')
                # update status
                appleImage.status = STARTED
                appleImage.setAutoDraw(True)
            
            # if appleImage is active this frame...
            if appleImage.status == STARTED:
                # update params
                pass
            
            # if appleImage is stopping this frame...
            if appleImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > appleImage.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    appleImage.tStop = t  # not accounting for scr refresh
                    appleImage.tStopRefresh = tThisFlipGlobal  # on global time
                    appleImage.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'appleImage.stopped')
                    # update status
                    appleImage.status = FINISHED
                    appleImage.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Feedback" ---
        for thisComponent in Feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Feedback
        Feedback.tStop = globalClock.getTime(format='float')
        Feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Feedback.stopped', Feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Feedback.maxDurationReached:
            routineTimer.addTime(-Feedback.maxDuration)
        elif Feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "RegretRating" ---
        # create an object to store info about Routine RegretRating
        RegretRating = data.Routine(
            name='RegretRating',
            components=[text, regret_key],
        )
        RegretRating.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for regret_key
        regret_key.keys = []
        regret_key.rt = []
        _regret_key_allKeys = []
        # Run 'Begin Routine' code from regretlogic
        # Show regret question only if:
        # participant_cond == 1 (Regret-First-30) AND
        # trial_num <= 30 AND
        # points == 0 (just lost)
        skip_regret = not (participant_cond == 1 and trial_num <= 30 and points == 0)
        if skip_regret:
            continueRoutine = False
            # We'll pre-log NA so each trial row has something
            thisExp.addData('regret_rating', 'NA')
            thisExp.addData('regret_rt', 'NA')
        # store start times for RegretRating
        RegretRating.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        RegretRating.tStart = globalClock.getTime(format='float')
        RegretRating.status = STARTED
        thisExp.addData('RegretRating.started', RegretRating.tStart)
        RegretRating.maxDuration = None
        # keep track of which components have finished
        RegretRatingComponents = RegretRating.components
        for thisComponent in RegretRating.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "RegretRating" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        RegretRating.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # *regret_key* updates
            waitOnFlip = False
            
            # if regret_key is starting this frame...
            if regret_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                regret_key.frameNStart = frameN  # exact frame index
                regret_key.tStart = t  # local t and not account for scr refresh
                regret_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(regret_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'regret_key.started')
                # update status
                regret_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(regret_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(regret_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if regret_key.status == STARTED and not waitOnFlip:
                theseKeys = regret_key.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], ignoreKeys=["escape"], waitRelease=False)
                _regret_key_allKeys.extend(theseKeys)
                if len(_regret_key_allKeys):
                    regret_key.keys = _regret_key_allKeys[-1].name  # just the last key pressed
                    regret_key.rt = _regret_key_allKeys[-1].rt
                    regret_key.duration = _regret_key_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                RegretRating.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RegretRating.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "RegretRating" ---
        for thisComponent in RegretRating.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for RegretRating
        RegretRating.tStop = globalClock.getTime(format='float')
        RegretRating.tStopRefresh = tThisFlipGlobal
        thisExp.addData('RegretRating.stopped', RegretRating.tStop)
        # check responses
        if regret_key.keys in ['', [], None]:  # No response was made
            regret_key.keys = None
        trials.addData('regret_key.keys',regret_key.keys)
        if regret_key.keys != None:  # we had a response
            trials.addData('regret_key.rt', regret_key.rt)
            trials.addData('regret_key.duration', regret_key.duration)
        # Run 'End Routine' code from regretlogic
        if not skip_regret:
            k = regret_key.keys
            if k in (None, ''):
                rating = 'NA'
            elif k == '0':
                rating = 10
            else:
                rating = int(k)
            thisExp.addData('regret_rating', rating)
            thisExp.addData('regret_rt', regret_key.rt)
        # the Routine "RegretRating" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ITI" ---
        # create an object to store info about Routine ITI
        ITI = data.Routine(
            name='ITI',
            components=[blank_screen],
        )
        ITI.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ITI
        ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ITI.tStart = globalClock.getTime(format='float')
        ITI.status = STARTED
        thisExp.addData('ITI.started', ITI.tStart)
        ITI.maxDuration = None
        # keep track of which components have finished
        ITIComponents = ITI.components
        for thisComponent in ITI.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ITI" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        ITI.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank_screen* updates
            
            # if blank_screen is starting this frame...
            if blank_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank_screen.frameNStart = frameN  # exact frame index
                blank_screen.tStart = t  # local t and not account for scr refresh
                blank_screen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank_screen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_screen.started')
                # update status
                blank_screen.status = STARTED
                blank_screen.setAutoDraw(True)
            
            # if blank_screen is active this frame...
            if blank_screen.status == STARTED:
                # update params
                pass
            
            # if blank_screen is stopping this frame...
            if blank_screen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank_screen.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    blank_screen.tStop = t  # not accounting for scr refresh
                    blank_screen.tStopRefresh = tThisFlipGlobal  # on global time
                    blank_screen.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blank_screen.stopped')
                    # update status
                    blank_screen.status = FINISHED
                    blank_screen.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ITI.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ITI
        ITI.tStop = globalClock.getTime(format='float')
        ITI.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ITI.stopped', ITI.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ITI.maxDurationReached:
            routineTimer.addTime(-ITI.maxDuration)
        elif ITI.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "EndScreen" ---
    # create an object to store info about Routine EndScreen
    EndScreen = data.Routine(
        name='EndScreen',
        components=[],
    )
    EndScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from end_experiment
    import numpy as np
    
    # Try to get columns from the trials loop if available
    try:
        ratings = trials.data.get('regret_rating', [])
    except Exception:
        # fallback to experiment-wide data (if loop object unavailable)
        ratings = thisExp.data.get('regret_rating', [])
    
    # clean & convert
    ratings_clean = []
    for r in ratings:
        if r not in ('NA', '', None):
            try:
                ratings_clean.append(float(r))
            except Exception:
                pass
    avg_regret = round(np.mean(ratings_clean), 2) if ratings_clean else 'N/A'
    
    # points
    try:
        pts = trials.data.get('points', [])
    except Exception:
        pts = thisExp.data.get('points', [])
    pts_clean = []
    for p in pts:
        if p not in ('', None):
            try:
                pts_clean.append(float(p))
            except Exception:
                pass
    total_points = int(np.sum(pts_clean)) if pts_clean else 0
    
    # store so they end up in the output row
    thisExp.addData('avg_regret', avg_regret)
    thisExp.addData('total_points', total_points)
    # store start times for EndScreen
    EndScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EndScreen.tStart = globalClock.getTime(format='float')
    EndScreen.status = STARTED
    thisExp.addData('EndScreen.started', EndScreen.tStart)
    EndScreen.maxDuration = None
    # keep track of which components have finished
    EndScreenComponents = EndScreen.components
    for thisComponent in EndScreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EndScreen" ---
    EndScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            EndScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EndScreen" ---
    for thisComponent in EndScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EndScreen
    EndScreen.tStop = globalClock.getTime(format='float')
    EndScreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('EndScreen.stopped', EndScreen.tStop)
    thisExp.nextEntry()
    # the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
