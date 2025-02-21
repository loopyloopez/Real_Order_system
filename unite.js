import express from "express"
import axios from "axios"
import bodyParser from "body-parser";
const port = 8000;


const app = express();




app.post("/new",(req,res)=>{

    res.send("thank you");
    console.log(req.body);



})

app.listen(port,()=>{
    console.log("lestening on port 8000");
})