import express, { json } from "express"
import bodyParser from "body-parser";
import fs from "fs";

const Express = express()

const app = express();
const port = 3000;
var orderID =1;
const dir = '/home/loopyloops/Documents/A.O.S/Real_Order_system/orders';

var file= fs.readdirSync(dir,(err,files)=>{
  if(err){
    console.error("erorr nig");
    return;
  }
});

var largest= 0;
for(let i = 0;i <= file.length; i++){
  try{
    if( parseInt(file[i].slice(5,6)) > largest){
    largest =  parseInt(file[i].slice(5,6));
    }
  }
  catch{
    console.log("no number found")
  }
 
  

}
console.log(largest);
orderID = largest + 1;

app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));




app.post("/new",(req,res)=>{
    
    
    res.render("/home/loopyloops/Documents/A.O.S/Real_Order_system/orderdone.ejs",{gmail:req.body["email"]})
   
    const content = req.body["name"] + "\n" +req.body["email"] + "\n" + req.body["orderDetails"] + "\n" + req.body["totalPrice"] + "\n";
    
    //making order txt file
    fs.writeFile('orders/order' + orderID +  '.txt', content, err => {
        if (err) {
          console.error(err);
        } else {
          // file written successfully
        }
      });

     //writing total for python file to read 
    fs.writeFile('orders/total.txt', orderID.toString(), err => {
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



