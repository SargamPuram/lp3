// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentRegistry {
    struct Student {
        string name;
        uint256 rollno;
        string class;
        address owner;
    }

    Student[] private students;

    function addStudent(string memory _name, uint256 _rollno, string memory _class) public {
        students.push(Student(_name, _rollno, _class, msg.sender));
    }

    function getTotalStudents() public view returns (uint256) {
        return students.length;
    }

    // safer: returns the Student struct instead of multiple strings
    function getStudentById(uint256 _id) public view returns (Student memory) {
        require(_id < students.length, "Student does not exist");
        return students[_id];
    }

    function updateStudent(uint256 _id, string memory _newName, string memory _newClass) public {
        require(_id < students.length, "Student does not exist");
        require(students[_id].owner == msg.sender, "You are not the owner of this record!");
        students[_id].name = _newName;
        students[_id].class = _newClass;
    }

    function deleteStudent(uint256 _id) public {
        require(_id < students.length, "Student does not exist");
        require(students[_id].owner == msg.sender, "You are not the owner of this record!");
        students[_id] = students[students.length - 1];
        students.pop();
    }

    fallback() external {
        revert("This is fallback function");
    }
}


