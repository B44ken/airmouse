# airmouse

airmouse is an experiment that allows you to use your phone to control your computer's mouse

but the accelerometer data is very noisy at mouse scale. we could:
- attempt to calibrate or deadzone the accelerometer data
- use touch/drag events instead
- rework it into a keyboard app instead
- see if gyroscope data is more accurate

## using
- launch the web server `server.py` (standard flask app). note that https is required for device motion api.
    - i use the script `run.sh`, just change `$SITE` to your website
- go to the server on your phone, and hit start. you may need to specify `https://SITE:443` (no auto redirection)
- launch `client.py` on the computer, and type in the code.

## dependencies
python: `flask`, `requests`, `pyautoguoi`
