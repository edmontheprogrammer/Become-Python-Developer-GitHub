// Creating arrays in Swift 
var perStudentPetCount = [0, 1, 0, 1, 2, 3, 4, 2, 3, 0,1]

var numOfStudents = perStudentPetCount.count

// sumOfItems / numOfStudents

print(perStudentPetCount[3])

// getting index out of bound error 
//print(perStudentPetCount[100])

// Getting the size of the array 
print(numOfStudents)

// Getting the sum of the contents of the array
// Getting the total of all the elements in the array
// using the for-in loop
var sum = 0
for individualPetCount in perStudentPetCount {
    sum = sum + individualPetCount
}

// printing the total 
print(sum)

// getting the average 
var average = sum / numOfStudents

// printing the average 
print(average)