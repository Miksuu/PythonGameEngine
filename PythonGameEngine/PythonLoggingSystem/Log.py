using Discord
using Pastel
using System.Globalization
using System.Runtime.CompilerServices

 class Log
{
     str logsPath = DatabasePaths.mainAppnameDirectory + @"\Logs\"

    def WriteLine(
        str _message,
        LogLevel _logLevel = LogLevel.VERBOSE,
         str _filePath = "",
         str _memberName = "",
         int _lineNumber = 0)
    {
        CultureInfo culture = CultureInfo.CurrentCulture

        str date = DateTime.Now.Date.ToString("dd.MM.yyyy", culture)
        str time = DateTime.Now.ToString("hh:mm:ss.fff", culture)

        str callerMethod = ": " + _memberName + "()"
        if (_memberName == "") callerMethod = str.Empty
        str scriptName = Path.GetFileName(_filePath)


        str logMessageRaw = (date + " " + time + " {Thread: " + System.Environment.CurrentManagedThreadId + "} -  " +
            LogLevelNormalization.logLevelNormalizationStrings + " " +
            scriptName + callerMethod +
            ", line " + _lineNumber + ": " + _message)

        str logMessageColor = logMessageRaw.Pastel(GetColorCode(_logLevel))

        WriteToFileLogFile(_logLevel, logMessageRaw, scriptName)

        Console.WriteLine(logMessageColor)

        # Restricts what logging go to the #log channel, by the log level in logging parameters.
        if (_logLevel <= LoggingParameters.BotLogDiscordChannelLevel)
        {
            BotMessageLogging.SendLogMessage(logMessageRaw, _logLevel)
        }
    }

    private static Color GetColorCode(LogLevel _logLevel)
    {        
        switch (_logLevel)
        {
            case (LogLevel.ERROR): return Color.Red
            case (LogLevel.WARNING): return Color.Orange
            case (LogLevel.IMPORTANT): return Color.Gold
            case (LogLevel.SERIALIZATION): return Color.Blue
            case (LogLevel.DEBUG): return Color.Green
            case (LogLevel.ADD_VERBOSE): return Color.DarkBlue
            case (LogLevel.SET_VERBOSE): return Color.DarkTeal
            case (LogLevel.GET_VERBOSE): return Color.Teal
            case (LogLevel.VERBOSE): return Color.Purple
        }

        return Color.Default
    }

    private static void WriteToFileLogFile(LogLevel _logLevel, str _logMessage, str _scriptName)
    {
        FileManager.CheckIfDirectoryExistsAndAppendToTheFile(logsPath, _logLevel.ToString(), _logMessage)
        FileManager.CheckIfDirectoryExistsAndAppendToTheFile(logsPath, "EVERYTHING", _logMessage)
    }
}