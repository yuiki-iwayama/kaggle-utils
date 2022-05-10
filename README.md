# kaggle-utils
This repository is convenient package for Kaggle Competitions.

# API credentials
**To use the Competition class, the following operations are required.**
1. To get started, sign up for a Kaggle account at https://www.kaggle.com.
2. Select "Create API Token" from the "Accounts" tab of the user profile (https://www.kaggle.com/<username>/account).
3. This will start the download of `kaggle.json`, the file containing the API credentials, and place it in `~/.kaggle/kaggle.json` (on Linux, OSX, and other UNIX-based operating systems) or `C:\Users<Windows-username>.kaggle\kaggle.json` (on Windows).
4. On Unix-based systems, run `chmod 600 ~/.kaggle/kaggle.json`

# Installation
- Please install git before installing with pip.
- `pip install git+https://github.com/yuiki-iwayama/kaggle-utils`

# LICENSE
- Subject to the MIT License

# References
- [How to Use Kaggle](https://www.kaggle.com/docs/api)
- [Kaggle/kaggle-api](https://github.com/Kaggle/kaggle-api)