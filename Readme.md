# COMP4801 Final Year Project - Backend

This is the implementation of the back-end of COMP4801, which is a Flask application for handling the HTTP request from the front-end.


## Usage

1. Create and activate a Python virtual environments by executing the following command or refering to <https://docs.python.org/3/tutorial/venv.html>

    ```python
    python -m venv venv
    ```

2. Install the dependencies by

    ```python
    pip install requirements.txt
    ```

3. Download the trained ML models (.pkl files) from <https://drive.google.com/drive/folders/19lsuaveqRE7FcAMYpC-M2YEDJ3M3K_J4?usp=sharing> as the size of these files is too large to upload to Github.

4. Run the application by

    ```python
    python main.py
    ```

5. Access <localhost:5000> for more details about the avaliable endpoints of this application or simply use <localhost:5000/classify?url=www.google.com> to classify the URL <www.google.com>. (You can change the URL to classify any URLs you want)