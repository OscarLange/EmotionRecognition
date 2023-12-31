#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.2),
    on November 05, 2023, at 16:06
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

circle_middle_x = 0.055
circle_middle_y = 0.005
out_circle_rad = 0.375
out_circle1_rad = 0.3
out_circle2_rad = 0.24
out_circle3_rad = 0.17
out_circle4_rad = 0.1
inner_circle = 0.04
pointx = 0.055
pointy = 0.46
point1x = 0.44
point1y = 0.31
point2x = 0.58
point2y = -0.11
point3x = 0.246
point3y = -0.39
point4x = -0.13
point4y = -0.398
point5x = -0.42
point5y = -0.103
point6x = -0.346
point6y = 0.299

def isInside(circle_x, circle_y, rad, x, y):
    # Compare radius of circle
    # with distance of its center
    # from given point
    if ((x - circle_x) * (x - circle_x) +
        (y - circle_y) * (y - circle_y) <= rad * rad):
        return True
    else:
        return False

def isInsideTriangle(x1,y1,x2,y2,x3,y3,xp,yp):
    c1 = (x2-x1)*(yp-y1)-(y2-y1)*(xp-x1)
    c2 = (x3-x2)*(yp-y2)-(y3-y2)*(xp-x2)
    c3 = (x1-x3)*(yp-y3)-(y1-y3)*(xp-x3)
    return (c1<0 and c2<0 and c3<0) or (c1>0 and c2>0 and c3>0)

def convertMouseInputToEmotion(x,y):
    if(isInside(circle_middle_x,circle_middle_y,out_circle_rad,x,y)):
        if(isInside(circle_middle_x,circle_middle_y,inner_circle,x,y)):
            print("No emotion")
        elif(isInside(circle_middle_x,circle_middle_y,out_circle4_rad,x,y)):
            print("Emotion=1")
        elif(isInside(circle_middle_x,circle_middle_y,out_circle3_rad,x,y)):
            print("Emotion=2")
        elif(isInside(circle_middle_x,circle_middle_y,out_circle2_rad,x,y)):
            print("Emotion=3")
        elif(isInside(circle_middle_x,circle_middle_y,out_circle1_rad,x,y)):
            print("Emotion=4")
        else:
            print("Emotion=5")

        if(isInsideTriangle(circle_middle_x,circle_middle_y,pointx,pointy,point1x,point1y,x,y)):
            print("Ueberaschung")
        elif(isInsideTriangle(circle_middle_x,circle_middle_y,point1x,point1y,point2x,point2y,x,y)):
            print("Ekel")
        elif(isInsideTriangle(circle_middle_x,circle_middle_y,point2x,point2y,point3x,point3y,x,y)):
            print("Trauer")
        elif(isInsideTriangle(circle_middle_x,circle_middle_y,point3x,point3y,point4x,point4y,x,y)):
            print("Aerger")
        elif(isInsideTriangle(circle_middle_x,circle_middle_y,point4x,point4y,point5x,point5y,x,y)):
            print("Angst")
        elif(isInsideTriangle(circle_middle_x,circle_middle_y,point5x,point5y,point6x,point6y,x,y)):
            print("Begeisterung")
        else:
            print("Freude")
    else:
        print("Outside circle")

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.2'
expName = 'test'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\lange\\Desktop\\FunProjects\\EmotionRecognition\\test.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "trial" ---
selection = visual.ImageStim(
    win=win,
    name='selection', 
    image='FeelingsCircleBigText.gimp.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text = visual.TextStim(win=win, name='text',
    text='Wie finden Sie das Video?',
    font='Open Sans',
    units='norm', pos=(-0.65, 0.6), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
movie = visual.MovieStim(
    win, name='movie',
    filename='TicTacToe.mp4', movieLib='ffpyplayer',
    loop=False, volume=1.0, noAudio=False,
    pos=(0, 0), size=(1, 0.8), units=win.units,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
    depth=-2
)
motivation = visual.Slider(win=win, name='motivation',
    startValue=0, size=(0.5, 0.1), pos=(0.65, -0.8), units='norm',
    labels=(0 ,1, 2, 3, 4, 5 ,6 ,7 ,8 ,9 ,10), ticks=(0 ,1, 2, 3, 4, 5 ,6 ,7 ,8 ,9 ,10), granularity=1.0,
    style='scrollbar', styleTweaks=(), opacity=None,
    labelColor='Black', markerColor='Black', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-3, readOnly=False)
Motivation = visual.TextStim(win=win, name='Motivation',
    text='Motivation',
    font='Open Sans',
    units='norm', pos=(0.65, -0.7), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "trial" ---
continueRoutine = True
# update component parameters for each repeat
motivation.reset()
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
trialComponents = [selection, text, movie, motivation, Motivation, mouse]
for thisComponent in trialComponents:
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

# --- Run Routine "trial" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *selection* updates
    
    # if selection is starting this frame...
    if selection.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        selection.frameNStart = frameN  # exact frame index
        selection.tStart = t  # local t and not account for scr refresh
        selection.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(selection, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'selection.started')
        # update status
        selection.status = STARTED
        selection.setAutoDraw(True)
    
    # if selection is active this frame...
    if selection.status == STARTED:
        # update params
        pass
    
    # if selection is stopping this frame...
    if selection.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > selection.tStartRefresh + 8.0-frameTolerance:
            # keep track of stop time/frame for later
            selection.tStop = t  # not accounting for scr refresh
            selection.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'selection.stopped')
            # update status
            selection.status = FINISHED
            selection.setAutoDraw(False)
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
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
    
    # if text is stopping this frame...
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 8.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            # update status
            text.status = FINISHED
            text.setAutoDraw(False)
    
    # *movie* updates
    
    # if movie is starting this frame...
    if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie.frameNStart = frameN  # exact frame index
        movie.tStart = t  # local t and not account for scr refresh
        movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'movie.started')
        # update status
        movie.status = STARTED
        movie.setAutoDraw(True)
        movie.play()
    
    # if movie is stopping this frame...
    if movie.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > movie.tStartRefresh + 9.0-frameTolerance:
            # keep track of stop time/frame for later
            movie.tStop = t  # not accounting for scr refresh
            movie.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'movie.stopped')
            # update status
            movie.status = FINISHED
            movie.setAutoDraw(False)
            movie.stop()
    
    # *motivation* updates
    
    # if motivation is starting this frame...
    if motivation.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        motivation.frameNStart = frameN  # exact frame index
        motivation.tStart = t  # local t and not account for scr refresh
        motivation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(motivation, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'motivation.started')
        # update status
        motivation.status = STARTED
        motivation.setAutoDraw(True)
    
    # if motivation is active this frame...
    if motivation.status == STARTED:
        # update params
        pass
    
    # Check motivation for response to end routine
    if motivation.getRating() is not None and motivation.status == STARTED:
        continueRoutine = False
    
    # *Motivation* updates
    
    # if Motivation is starting this frame...
    if Motivation.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        Motivation.frameNStart = frameN  # exact frame index
        Motivation.tStart = t  # local t and not account for scr refresh
        Motivation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Motivation, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Motivation.started')
        # update status
        Motivation.status = STARTED
        Motivation.setAutoDraw(True)
    
    # if Motivation is active this frame...
    if Motivation.status == STARTED:
        # update params
        pass
    
    # if Motivation is stopping this frame...
    if Motivation.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Motivation.tStartRefresh + 8.0-frameTolerance:
            # keep track of stop time/frame for later
            Motivation.tStop = t  # not accounting for scr refresh
            Motivation.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Motivation.stopped')
            # update status
            Motivation.status = FINISHED
            Motivation.setAutoDraw(False)
    # *mouse* updates
    
    # if mouse is starting this frame...
    if mouse.status == NOT_STARTED and t >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse.started', t)
        # update status
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    
    # if mouse is stopping this frame...
    if mouse.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mouse.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            mouse.tStop = t  # not accounting for scr refresh
            mouse.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mouse.stopped', t)
            # update status
            mouse.status = FINISHED
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = mouse.getPos()
                convertMouseInputToEmotion(x,y)
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial" ---
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
movie.stop()
thisExp.addData('motivation.response', motivation.getRating())
thisExp.addData('motivation.rt', motivation.getRT())
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.nextEntry()
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
