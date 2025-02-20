import express from "express"
import bodyParser from "body-parser";
import fs from "fs";
const Express = express()

const app = express();
const port = 3000;
var orderID =1;

app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));
app.get("/",(req,res)=>{
    res.sendFile("/Users/ericklopez/Documents/canistillremember/main.html");
    
})
app.post("/new",(req,res)=>{
    console.log(req.body);
    res.send("<h1>Thank you <h1>");
   
    const content = req.body["name"] + "\n" +req.body["email"] + "\n" + req.body["orderDetails"] + "\n" + req.body["totalPrice"] + "\n";
    console.log(typeof content);
    //making order txt file
    fs.writeFile('/Users/ericklopez/Documents/canistillremember/orders/order' + orderID +  '.txt', content, err => {
        if (err) {
          console.error(err);
        } else {
          // file written successfully
        }
      });

     //writing total for python file to read 
    fs.writeFile('/Users/ericklopez/Documents/canistillremember/orders/total.txt', orderID.toString(), err => {
        if (err) {
          console.error(err);
        } else {
          // file written successfully
        }
      });
    orderID ++;

})



app.listen(port,'0.0.0.0',() =>{
    console.log("lestining on port" + port.toString());

})