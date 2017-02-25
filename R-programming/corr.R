# Write a function that takes a directory of data files and a threshold for complete cases and 
# calculates the correlation between sulfate and nitrate for monitor locations where the number of 
# completely observed cases (on all variables) is greater than the threshold. The function should 
# return a vector of correlations for the monitors that meet the threshold requirement. If no 
# monitors meet the threshold requirement, then the function should return a numeric vector of length 0.

corr <- function(directory, threshold = 0 ) {
    corr.list <- NULL
    id <- 1:332
    dat <- NULL
    for(i in id){
        fid <- sprintf("%03d",i)
        filename <- paste(directory,"/",fid,".csv",sep="")
        dat <- read.csv(filename)
        src <- na.omit(dat)              # omit NA'
        dat <- src
        len <- length(dat$ID);
        if(len > threshold && threshold >=0 ){
            corr.re <- cor(dat$sulfate, dat$nitrate)
            corr.list=c(corr.list, corr.re)
        }
    }
    corr.list
}



