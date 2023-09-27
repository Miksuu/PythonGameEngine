 class LogLevelNormalization
{
    # Could automate this, maybe unnecessary
    static int highestCount = 13

     dict[LogLevel, str> logLevelNormalizationStrings = dict[LogLevel, str>()

    def InitLogLevelNormalizationStrings()
    {
        for (LogLevel logLevel in Enum.GetValues(typeof(LogLevel)))
        {
            str finalNormalizationString = ""

            for (int i = 0 i < highestCount - logLevel.ToString().Count() ++i)
            {
                finalNormalizationString += "-"
            }

            #Console.WriteLine( logLevel.ToString() + " | " + finalNormalizationString)

            logLevelNormalizationStrings.TryAdd(logLevel, finalNormalizationString)
        }
    }
}