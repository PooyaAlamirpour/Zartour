$(document).ready(function() {

	/****************************
	*      Basic Scenario       *
	****************************/

	$("#basicScenario").jsGrid({
	width: "100%",
	filtering: false,
	editing: true,
	inserting: false,
	sorting: true,
	paging: true,
	autoload: true,
	pageSize: 15,
	pageButtonCount: 5,
	pagerFormat: "{first} {prev}  {pages} {next} {last}",
	pagePrevText: "<i class='icon-angle-right'></i>",
	pageNextText: "<i class='icon-angle-left'></i>",
		pageFirstText: "<i class='icon-angle-double-right'></i>",
		pageLastText: "<i class='icon-angle-double-left'></i>",
	deleteConfirm: "داده مورد نظر حذف شود ؟",
	controller: db,
	fields: [
		{ name: "Name", type: "text", width: 150 },
		{ name: "Age", type: "number", width: 50 },
		{ name: "Address", type: "text", width: 200 },
		{ name: "Country", type: "select", items: db.countries, valueField: "Id", textField: "Name" },
		{ name: "Married", type: "checkbox", title: "Is Married", sorting: false },
		{ type: "control" }
	]
	});
});
