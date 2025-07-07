//finds all students
db.students.find()

//adds new student
db.students.insertOne({firstName: "Luke", lastName: "Skywalker", studentId: "s1019", houseId: "h1011"})

//updates student
db.students.updateOne({studentId: "s1019"}, {$set:{houseId: "h1012"}})

//deletes student
db.students.deleteOne({studentId: "s1019"})

//groups students by house
db.students.aggregate([{$group:{_id: "$houseId", students:{$push: "$$ROOT"}}}])

//groups students by specific house
db.students.aggregate([{$match:{houseId:'h1007'}}, {$group:{_id:"$houseId", students:{$push:"$$ROOT"}}}])

//groups students by mascot
db.students.aggregate([{$lookup:{from:"houses", localField:"houseId", foreignField: "houseId", as:"house"}}, {$match:{"house.mascot": "Eagle"}}, {$group:{_id: "$house.mascot", Students:{$push:"$$ROOT"}}}, {$project:{Students:1}}])
