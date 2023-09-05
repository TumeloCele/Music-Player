from cx_Freeze import setup, Executable

# Define the script to be converted to an executable
script = 'Player.py'

# Configure the build
build_options = {
    'build_exe': {
        'packages': [],  # List any additional packages your script depends on
    },
}

# Create the executable
executables = [Executable(script)]

setup(
    name='file explorer.py',   # Change this to the name of your application
    version='1.0',     # Change this to your application's version
    description='My Python Script',
    options=build_options,
    executables=executables
)
