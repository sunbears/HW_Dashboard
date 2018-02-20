var select = document.getElementById("selDataset");

// var options = ["BB_940", "BB_941"];
// for(var i = 0; i < options.length; i++) {
//     var opt = options[i];
//     var el = document.createElement("option");
//     el.text = opt;
//     el.value = opt;
//     select.append(el);
// }


// This function will get called from the dropdown event handler.
function optionChanged() {
    var sample = "";
    // Retrieve the value of the dropdown menu
    var sample = document.getElementById('selDataset').value;
    console.log(sample);
}

// var myObj = { "name":"John", "age":30, "car":null };
// for (x in myObj) {
//     document.getElementById("metadata").innerHTML += myObj[x] + "<br>";
// }


function buildPlot() {
    /* data route */
    var url = "/pie";
    Plotly.d3.json(url, function (error, data) {
        if (error) return console.warn(error);
        console.log(data);
        var layout = {
            title: "Top Ten Bacteria",
            showlegend: true,
            height: 600,
            // width: 980,
        };
        Plotly.newPlot("pie", data, layout);
    });
}

buildPlot();

// Plotly.d3.json('/pie', function(error, data){
//     if (error) return console.warn(error);

//     var layout = {
//         title: "Lyric Frequency"
//     }

//     Plotly.plot("pie", data, layout);
// })

// function updateMetaData() {
//     for (x in metadata_filtered){
//         document.getElementById("metadata").innerHTML += metadata_filtered[x]+"<br>";
//     }
// }
// updateMetaData();

// function buildPlot(){
//     var url='/wfreq/<sample>'
//     Plotly.d3.json(url, function(error, data){
//         if (error) return console.warn(error);
//         var layout = {
//             title = "Top Ten Bacteria Counts"
//         }
//         Plotly.plot("pie", data, layout);
//     })

// }