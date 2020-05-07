# simple-discord-spam

##Requirements
- Python 
    - selenium
- chromedriver

You can install python pretty easily. After you have python, open up terminal/command prompt/powershell and run:
`pip install selenium`

To install chromedriver, go to https://chromedriver.chromium.org/downloads and download the appropriate release for your version of Chrome. Once you have that, add it to your environment variables. Here's a link if you are having trouble: https://zwbetz.com/download-chromedriver-binary-and-add-to-your-path-for-automated-functional-testing/

##How to Use
When you are ready, just open up terminal/command prompt/powershell and navigate to the folder you saved this into. Then run the command:
`python pokespam.py`

I've set it so that once it pulls up the login page, you have 40 seconds to login and get to the channel you want to spam. You can change this time limit and other settings by modifying the python script. 