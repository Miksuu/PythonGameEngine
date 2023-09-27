class LogLevelNormalization:
    # Could automate this, maybe unnecessary
    readonly static highestCount = 13
    # Failed to translate method: public static Dictionary<LogLevel, string> logLevelNormalizationStrings = new Dictionary<LogLevel, string>();
    def InitLogLevelNormalizationStrings(self):
    foreach (LogLevel logLevel in Enum.GetValues(typeof(LogLevel)))
    finalNormalizationString = ""
    for (i = 0 i < highestCount - logLevel.ToString().Count() ++i)
    finalNormalizationString += "-";
    #Console.WriteLine( logLevel.ToString() + " | " + finalNormalizationString);
    logLevelNormalizationStrings.TryAdd(logLevel, finalNormalizationString);
