
install.packages("ggplot2")
library("ggplot2")

data = read.delim("data2.txt", header = TRUE, sep = "\t", dec = ".")
View(data)
colnames(data)

data$Date <- substr(data$Date, 1, 10)
summary(data$Date)
data$Date <- as.Date(data$Date,format="%Y-%m-%d")
summary(data$Date)
plot(x = data$Date, y = data$Error_Count)

library("ggplot2")
ggplot(data) +
  aes(x=Date,y=data$Error_Count) +
  geom_point() + 
  theme_bw() +
  labs(x="Time",y="# of Grammatical Errors",
       title="Grammatical Errors in Inklings Features Articles Over Time")

fit = lm(data$Error_Count ~ Date, data = data)
summary(fit)
resd = resid(fit)
plot(data$Date, resd,
     ylab="Residuals", xlab="Time")
ggplot(data) +
  aes(x=Date,y=resd) +
  geom_point() +
  theme_bw() +
  labs(x="Time", y="Residuals")
