#!/usr/bin/env bash
cd ../ui
ls | gawk -F . '{print "pyside-uic ../ui/" $1 ".ui > ../src/PlayblastBot/View/" $1 "_view.py && sed -i 1,8d ../src/PlayblastBot/View/" $1 "_view.py"}' > ../sh/ui_generator_playblast_bot.sh
ls | gawk -F . '{print "/usr/autodesk/maya2018/bin/mayapy /usr/autodesk/maya2018/bin/pyside2-uic ../ui/" $1 ".ui > ../src/PlayblastBot/View2/" $1 "_view2.py && sed -i 1,8d ../src/PlayblastBot/View2/" $1 "_view2.py"}' > ../sh/ui_generator_playblast_bot2.sh