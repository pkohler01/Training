/*Add the JavaScript here for the function billingFunction().  It is responsible for setting and clearing the fields in Billing Information */
function billingFunction{
  if(document.querySelector("#same").checked) {
    var shippingName = document.querySelector("#shippingName").value; //value entered into 'Name' shipping field
    var shippingZip = document.querySelector("#shippingZip").value; //value entered into 'Zip code' shipping field
    
    /* setting Billing info to match Shipping info due to checkbox being checked */
    document.querySelector('#billingName').value = shippingName;
    document.querySelector('#billingZip').value = shippingZip;
  } else { 
    /* if the checkbox isn't checked */
    document.querySelector('#billingName').value = shippingName;
    document.querySelector('#billingZip').value = shippingZip;    
  }
    
}