/**
 * Will Southard
 * WEB 335
 * Assignment 6.2 - Aggregate Queries (Hands-On 6.1)
 */

// a. Display all students. (Hands-On 6.1a)
db.students.find();

// b. Add a new student; then prove it was added. (Hands-On 6.1b)
db.students.insertOne({
  // IMPORTANT: match the existing fields from your students collection
  // TIP: run db.students.findOne() first to see the exact field names
  firstName: "Will",
  lastName: "Southard",
  studentId: "s9999",
  houseId: "h1000", // <-- adjust to a real houseId from db.houses.find()
  dateCreated: new Date()
});
db.students.findOne({ studentId: "s9999" });

// c. Update one property from the student you added; then prove it. (Hands-On 6.1c)
db.students.updateOne(
  { studentId: "s9999" },
  { $set: { lastName: "Southard-Updated" } }
);
db.students.findOne({ studentId: "s9999" });

// d. Delete the student you created; then prove it was removed. (Hands-On 6.1d)
db.students.deleteOne({ studentId: "s9999" });
db.students.findOne({ studentId: "s9999" });

// e. Display all students by house (Order: Houses -> Students). (Hands-On 6.1e)
db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "student_docs"
    }
  }
]);

// f. Display all students in house Gryffindor (Order: Gryffindor -> Students). (Hands-On 6.1f)
db.houses.aggregate([
  { $match: { name: "Gryffindor" } },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "student_docs"
    }
  }
]);

// g. Display all students in the house with an Eagle mascot (Order: House -> Students). (Hands-On 6.1g)
db.houses.aggregate([
  { $match: { mascot: "Eagle" } },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "student_docs"
    }
  }
]);