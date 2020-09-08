# Winerror

Simple and fast tool to get error descriptions in Windows Programming.


## Why

When you are programming to Windows platforms you often will get errors that you retrieved by calling ***GetLastError()*** function, with that code you can call the [FormatMessage](https://docs.microsoft.com/en-us/windows/desktop/api/WinBase/nf-winbase-formatmessage) function to get the string representation or go to the [System error code page](https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes) from Microsoft to understand what happened, with this tool is just a matter to create a local database for quick lookup and pass the error code to this software.



## What this do
* Crawl the System error page from microsoft
* Create a json representation using the error code as key
* Compress using zlib on your computer

### Examples
```
~ >>> winerror 15                                                              
Error code: 15
	Value: ERROR_INVALID_DRIVE
	Description: 15 (0xF)
```

Just that simple.


## Install

### Linux

* You just need to run ***install.sh***

### Windows

* You just need to run ***install.bat***

### That's all.

Thanks
