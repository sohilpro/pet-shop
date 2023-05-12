const numberFormat = (number) => {
  return new Intl.NumberFormat().format(number);
};
const toTitleCase = (str) => {
  return str.replace(/\w\S*/g, function (txt) {
    return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
  });
};
const totalShippingCost = (totalAmount) => {
  return totalAmount + 25000;
};
export { numberFormat, toTitleCase, totalShippingCost };
