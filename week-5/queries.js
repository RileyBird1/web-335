//create new user
db.users.insertOne({
  firstName: "John",
  lastName: "Smith",
  employeeId: "1013",
  email: "jsmith@me.com",
  dateCreated: new Date()
});

//updating mozarts email address
db.users.updateOne(
  { firstName: "Wolfgang", lastName: "Mozart" },
  { $set: { email: "mozart@me.com" } }
);

//displaying all users with new
db.users.find(
  {},
  { firstName: 1, lastName: 1, email: 1, _id: 0 }
)