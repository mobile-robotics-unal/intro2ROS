## Develop tricks

Section to add random information that might be useful.

## catkin_make vs catkin build?

Concensous is that catkin build is a more powerful and complete tool than catkin_make. The project was build using cat build and  [migration tutorial](https://catkin-tools.readthedocs.io/en/latest/migration.html)

## vscode setup

vscode comes with many handy extensions that help in the development process this are some of the extension used in this project:

```json
"extensions": [        
        "ms-iot.vscode-ros",
        "ms-python.debugpy",
        "ms-python.python",
        "ms-python.vscode-pylance",
        "eamodio.gitlens",
        "ms-vscode.cpptools",
        //"DavidAnson.vscode-markdownlint",
        "yzhang.markdown-all-in-one"
    ]

```

### vscode settings

A small detail that bugged me was that pylance show a warning when importing `rospy`to fix it you need to include the paths in pylance's context in settings.

````json
"python.autoComplete.extraPaths": [
    "{workspaceFolder}/devel/lib/python3/dist-packages",
    "/opt/ros/noetic/lib/python3/dist-packages"
]
```
## catkin tools


```
wstool update
```