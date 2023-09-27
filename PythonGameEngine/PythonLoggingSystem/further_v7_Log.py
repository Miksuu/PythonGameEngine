class Log:
    # Failed to translate method: public static string logsPath = DatabasePaths.mainAppnameDirectory + @"\Logs\";
    def WriteLine(self):
    _message,
    LogLevel _logLevel = LogLevel.VERBOSE,
    [CallerFilePath] _filePath = "",
    [CallerMemberName] _memberName = "",
    [CallerLineNumber] _lineNumber = 0)
    CultureInfo culture = CultureInfo.CurrentCulture;
    date = DateTime.Now.Date.ToString("dd.MM.yyyy", culture)
    time = DateTime.Now.ToString("hh:mm:ss.fff", culture)
    callerMethod = ": " + _memberName + "()"
    if (_memberName == "") callerMethod = string.Empty;
    scriptName = Path.GetFileName(_filePath)
    logMessageRaw = (date + " " + time + " {Thread: " + System.Environment.CurrentManagedThreadId + "} - [LOG | " + _logLevel + "] " +
    LogLevelNormalization.logLevelNormalizationStrings[_logLevel] + " " +
    scriptName + callerMethod +
    ", line " + _lineNumber + ": " + _message);
    logMessageColor = logMessageRaw.Pastel(GetColorCode(_logLevel))
    WriteToFileLogFile(_logLevel, logMessageRaw, scriptName);
    Console.WriteLine(logMessageColor);
    # Restricts what logging go to the #log channel, by the log level in logging parameters.
    if (_logLevel <= LoggingParameters.BotLogDiscordChannelLevel)
    BotMessageLogging.SendLogMessage(logMessageRaw, _logLevel);
    def GetColorCode(self):
    switch (_logLevel)
    case (LogLevel.ERROR): return Color.Red;
    case (LogLevel.WARNING): return Color.Orange;
    case (LogLevel.IMPORTANT): return Color.Gold;
    case (LogLevel.SERIALIZATION): return Color.Blue;
    case (LogLevel.DEBUG): return Color.Green;
    case (LogLevel.ADD_VERBOSE): return Color.DarkBlue;
    case (LogLevel.SET_VERBOSE): return Color.DarkTeal;
    case (LogLevel.GET_VERBOSE): return Color.Teal;
    case (LogLevel.VERBOSE): return Color.Purple;
    return Color.Default
    def WriteToFileLogFile(self):
    FileManager.CheckIfDirectoryExistsAndAppendToTheFile(logsPath, _logLevel.ToString(), _logMessage);
    FileManager.CheckIfDirectoryExistsAndAppendToTheFile(logsPath, "EVERYTHING", _logMessage);
