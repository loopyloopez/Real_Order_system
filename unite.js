import express from "express"
import axios from "axios"
import bodyParser from "body-parser";
const port = 8000;

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));



app.post("/new",(req,res)=>{

    res.send("thank you");
    const content = req.body["name"] + "\n" +req.body["email"] + "\n" + req.body["orderDetails"] + "\n" + req.body["totalPrice"] + "\n";
    console.log(req.body["name"]);
    console.log("ordered received");



})

app.listen(port,()=>{
    console.log("lestening on port 8000");
})