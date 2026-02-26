/**
 * Title: Southard-handsOn5_1.js
 * Author: Will Southard
 * Description: Hands-On 5.1 - MongoDB Document Manipulation and Projections
 */

// ------------------------------------------------------------
// a. Add a new user to the users collection and prove it was added.
// ------------------------------------------------------------

// Insert a new user document (ensure these fields match the existing collection fields).
db.users.insertOne({
    firstName: "Will",
    lastName: "Southard",
    employeeId: 2026,
    email: "will.southard@me.com",
    dateCreated: new Date()
  });
  
  // Prove the new user was added successfully.
  db.users.findOne({ employeeId: 2026 });
  
  // ------------------------------------------------------------
  // b. Update Mozart’s email address to mozart@me.com and prove it was updated.
  // ------------------------------------------------------------
  
  // Update the email for the user with lastName "Mozart".
  db.users.updateOne(
    { lastName: "Mozart" },
    { $set: { email: "mozart@me.com" } }
  );
  
  // Prove Mozart’s document was updated.
  db.users.findOne(
    { lastName: "Mozart" },
    { _id: 0, firstName: 1, lastName: 1, email: 1 }
  );
  
  // ------------------------------------------------------------
  // c. Display all users using projections (firstName, lastName, email only).
  // ------------------------------------------------------------
  
  db.users.find(
    {},
    { _id: 0, firstName: 1, lastName: 1, email: 1 }
  );