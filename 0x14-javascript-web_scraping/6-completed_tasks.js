#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, reaponse, body) {
    if (err) {
	console.log(err);
    } else if (response.statusCode === 200) {
	let completed = {};
	let tasks = JSON.parse(body);
	for (let i in tasks) {
	    let taks = tasks[i];
	    if (task.completed === true) {
		if (completed[task.userId] === undefined) {
		    completed[task.userId] = 1;
		} else {
		    completed[task.userId]++;
		}
	    }
	} console.log(completed);
    } else {
	console.log('An error occured. Statsu code: ' + response.statusCode);
    }
});
