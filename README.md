Changing Desktop wallpaper after turning on Windows every time with Python.

Set the script to run after Windows starts

 Save the script as a change_wallpaper.py file.
 Create a BAT file to run the Python script:

 pythonw C:\Path\To\Your\Script\change_wallpaper.py

 In Windows, go to Task Scheduler.
 Create a new task:
 In the Trigger section, select the "At startup" option.
 In the Action section, select the BAT file you created.

In this way, every time Windows starts, the desktop image will change automatically.
