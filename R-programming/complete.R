# Write a function that reads a directory full of files and reports the number of 
# completely observed cases in each data file. The function should return a data frame 
# where the first column is the name of the file and the second column is the number of complete cases. 


complete <- function(directory, id = 1:332) {
    
    directory <- "/Users/Lotusjiang/Desktop/DataScience /Course 2 R programming/specdata"
    files <- list.files(directory, full.names  = TRUE)
    dat <- data.frame()
    
    for (i in id){
        file_i <- read.csv(files[i])
        nobs <- sum(complete.cases(file_i))
        temp <- data.frame(i, nobs)
        dat <- rbind(dat, temp)
    }
    colnames(dat) <- c("id", "nobs")
    dat
}

# Test    
# complete("specdata", 1)


