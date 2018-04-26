var page = (function() {
  var dollarsPerTroyOunce = 1;

  function getGoldData() {
    // TODO: Make current date
    httpGetAsync(
      "https://www.quandl.com/api/v3/datasets/LBMA/GOLD.json?api_key=yohchH9Uyg7_EzdN6cJP&column_index=2&start_date=2018-04-19&end_date=2018-04-24",
      response => {
        console.log(response.dataset.data[0][1]);
        dollarsPerTroyOunce = response.dataset.data[0][1];
      }
    );
  }

  function clickedEnter() {
    let pounds = document.getElementById("weightField").value;
    let url = `/api/convert/?from=lbs&to=t_oz&value=${pounds}`;
    httpGetAsync(url, response => {
      console.log(response);
      let text = document.createElement("p");
      text.id = "text";
      let dollarValue = response.value * dollarsPerTroyOunce;
      text.innerHTML = `${pounds} pounds of gold is worth $${dollarValue}`;
      let body = document.getElementById("body");
      if (document.getElementById("text") != undefined) {
        body.removeChild(document.getElementById("text"));
      }
      body.appendChild(text);
    });
  }

  function httpGetAsync(theUrl, callback) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4 && xhr.status == 200) {
        callback(JSON.parse(xhr.responseText));
      }
    };
    xhr.open("GET", theUrl, true);
    xhr.send(null);
  }

  window.onload = getGoldData();

  return {
    clickedEnter: clickedEnter
  };
})();
