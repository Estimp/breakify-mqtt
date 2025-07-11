# Breakify - MQTT Consumer

This repository contains two .exe files: one that launches with a console to display the logs, and another that runs without showing the console.

If you want to modify the project, the source code is also included in the repository so you can download and customize it.

> Optional: On Windows 10, if you want the .exe to start automatically when the system boots, you can place it in the following folder: `%ProgramData%\Microsoft\Windows\Start Menu\Programs\Startup`.
>
> Any .exe placed in that folder will run automatically when Windows starts.

This project is part of a larger system called Breakify. The Android app for Breakify can be found in the following repository: [breakify-android-releases](https://github.com/Estimp/breakify-android-releases/tree/main)

## Project Architecture
Breakify consists of multiple independent services:

| Component       | Repository                          | Description                  |
|-----------------|-------------------------------------|------------------------------|
| Android App | [breakify-android-releases](https://github.com/Estimp/breakify-android-releases/tree/main) | Compiled APK releases |
| API Service | [breakify-service](https://github.com/Estimp/breakify-service) | Back-end RESTful API |
| **MQTT Message Consumer** | **This repository** | Subscribes and processes MQTT messages |
