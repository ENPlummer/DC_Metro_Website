// Create a dropdown menu for average Metro ridershio.

console.log("Hello World!");


d3.json("/top25stationsaverage", function(top25AverageData) {
		//console.log(stationData);

		stations = top25AverageData[0];
		averages = top25AverageData[1];
		//console.log(stations);
		//console.log(averages);

	var trace1 = [{
		x: stations,
		y: averages,
		type: "bar"
	}];

	Plotly.newPlot("top25averageplot", trace1);
 });

d3.json("/bottom25stationsaverage", function(bottom25AverageData) {
		bottom_25_stations = bottom25AverageData[0];
		bottom_25_averages = bottom25AverageData[1];

	var trace2 = [{
		x: bottom_25_stations,
		y: bottom_25_averages,
		type: "bar"
	}];

	Plotly.newPlot("bottom25averageplot", trace2);
});

d3.json("/top25stationstotal", function(top25MetroStationsData){
		top25MetroStationsNames = top25MetroStationsData[0];
		top25MetroStationsTotals = top25MetroStationsData[1];

	var trace3 = [{
		x: top25MetroStationsNames,
		y: top25MetroStationsTotals,
		type: "bar"
	}];

	Plotly.newPlot("top25totalplot", trace3);
});

d3.json("/bottom25stationstotal", function(bottom25MetroStationsData) {
		bottom25MetroStationsNames = bottom25MetroStationsData[0];
		bottom25MetroStationsTotals = bottom25MetroStationsData[1];

		var trace4 = [{
			x: bottom25MetroStationsNames,
			y: bottom25MetroStationsTotals,
			type: "bar"
		}];

		Plotly.newPlot("bottom25totalplot", trace4);
});

d3.json("/timeperiodaverage", function(averageTimePeriodData) {
		timePeriods = averageTimePeriodData[0];
		timePeriodAverages = averageTimePeriodData[1];

	var trace5 = [{
		labels: timePeriods,
		values: timePeriodAverages,
		type: "pie"
	}];

	Plotly.newPlot("piechartaverage", trace5);

});

d3.json("/timeperiodridershiptotal", function(totalTimePeriodData) {
		metroTimePeriods = totalTimePeriodData[0];
		metroTimePeriodsTotals = totalTimePeriodData[1];

	var trace6 = [{
		labels: metroTimePeriods,
		values: metroTimePeriodsTotals,
		type: "pie"
	}];

	Plotly.newPlot("totalridershippiechart", trace6);

});
