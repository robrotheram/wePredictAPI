/*
 * Author: Abdullah A Almsaeed
 * Date: 4 Jan 2014
 * Description:
 *      This is a demo file used only for the main dashboard (index.html)
 **/

$(function () {
    "use strict";

    $('.daterange').daterangepicker(
        {
            ranges: {
                'Today': [moment(), moment()],
                'Yesterday': [moment().subtract('days', 1), moment().subtract('days', 1)],
                'Last 7 Days': [moment().subtract('days', 6), moment()],
                'Last 30 Days': [moment().subtract('days', 29), moment()],
                'This Month': [moment().startOf('month'), moment().endOf('month')],
                'Last Month': [moment().subtract('month', 1).startOf('month'), moment().subtract('month', 1).endOf('month')]
            },
            startDate: moment().subtract('days', 29),
            endDate: moment()
        },
        function (start, end) {
            alert("You chose: " + start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
        });

    /* jQueryKnob */
    $(".knob").knob();

    //jvectormap data
    var visitorsData = {
        "UKL": 398, //USA
        "UKS": 400, //Saudi Arabia
        "UKD": 1000, //Canada
        "UKW": 500}

    $('#world-map').vectorMap({
        map: 'uk_mill_en',
        backgroundColor: "transparent",
        regionStyle: {
            initial: {
                fill: '#e4e4e4',
                "fill-opacity": 1,
                stroke: 'none',
                "stroke-width": 0,
                "stroke-opacity": 1
            }
        },
        series: {
            regions: [
                {
                    values: visitorsData,
                    scale: ["#92c1dc", "#ebf4f9"],
                    normalizeFunction: 'polynomial'
                }
            ]
        }
    });


    //Sparkline charts
    var myvalues = [1000, 1200, 920, 927, 931, 1027, 819, 930, 1021];
    $('#sparkline-1').sparkline(myvalues, {
        type: 'line',
        lineColor: '#92c1dc',
        fillColor: "#ebf4f9",
        height: '50',
        width: '80'
    });
    myvalues = [515, 519, 520, 522, 652, 810, 370, 627, 319, 630, 921];
    $('#sparkline-2').sparkline(myvalues, {
        type: 'line',
        lineColor: '#92c1dc',
        fillColor: "#ebf4f9",
        height: '50',
        width: '80'
    });
    myvalues = [15, 19, 20, 22, 33, 27, 31, 27, 19, 30, 21];
    $('#sparkline-3').sparkline(myvalues, {
        type: 'line',
        lineColor: '#92c1dc',
        fillColor: "#ebf4f9",
        height: '50',
        width: '80'
    });

    //The Calender
    $("#calendar").datepicker();

    //SLIMSCROLL FOR CHAT WIDGET
    $('#chat-box').slimScroll({
        height: '250px'
    });


    $.getJSON("/v1/getcopdaverage", function (json) { // callback function which gets called when your request completes.
        var line = new Morris.Line({
            element: 'line-chart',
            resize: true,
            data: json,
            xkey: 'y',
            ykeys: ['value_y'],
            labels: ['Item value_y'],
            lineColors: ['#efefef'],
            lineWidth: 2,
            hideHover: 'auto',
            gridTextColor: "#fff",
            gridStrokeWidth: 0.4,
            pointSize: 4,
            pointStrokeColors: ["#efefef"],
            gridLineColor: "#efefef",
            gridTextFamily: "Open Sans",
            gridTextSize: 10
        });
    });


    $.getJSON("/v1/get_copd_ASTHMA_average", function (jsonData) { // callback function which gets called when your request completes.
        /* Morris.js Charts */
        // Sales chart
        var area = new Morris.Area({
            element: 'revenue-chart',
            resize: true,
            data: jsonData,
            xkey: 'y',
            ykeys: ['value_COPD', 'value_ASMTHA'],
            labels: ['COPD', 'ASMTHA'],
            lineColors: ['#a0d0e0', '#3c8dbc'],
            hideHover: 'auto'
        });
    });

    /*Bar chart
     var bar = new Morris.Bar({
     element: 'bar-chart',
     resize: true,
     data: [
     {y: '2006', a: 100, b: 90},
     {y: '2007', a: 75, b: 65},
     {y: '2008', a: 50, b: 40},
     {y: '2009', a: 75, b: 65},
     {y: '2010', a: 50, b: 40},
     {y: '2011', a: 75, b: 65},
     {y: '2012', a: 100, b: 90}
     ],
     barColors: ['#00a65a', '#f56954'],
     xkey: 'y',
     ykeys: ['a', 'b'],
     labels: ['CPU', 'DISK'],
     hideHover: 'auto'
     });*/
    //Fix for charts under tabs
    $('.box ul.nav a').on('shown.bs.tab', function (e) {
        area.redraw();
        donut.redraw();
    });


    /* BOX REFRESH PLUGIN EXAMPLE (usage with morris charts) */
    $("#loading-example").boxRefresh({
        source: "ajax/dashboard-boxrefresh-demo.php",
        onLoadDone: function (box) {
            var bar = new Morris.Bar({
                element: 'bar-chart',
                resize: true,
                data: [
                    {y: '2006', a: 100, b: 90},
                    {y: '2007', a: 75, b: 65},
                    {y: '2008', a: 50, b: 40},
                    {y: '2009', a: 75, b: 65},
                    {y: '2010', a: 50, b: 40},
                    {y: '2011', a: 75, b: 65},
                    {y: '2012', a: 100, b: 90}
                ],
                barColors: ['#00a65a', '#f56954'],
                xkey: 'y',
                ykeys: ['a', 'b'],
                labels: ['CPU', 'DISK'],
                hideHover: 'auto'
            });
        }
    });

    /* The todo list plugin */
    $(".todo-list").todolist({
        onCheck: function (ele) {
            //console.log("The element has been checked")
        },
        onUncheck: function (ele) {
            //console.log("The element has been unchecked")
        }
    });


    /* vector map */


    var width = $("#map").width(),
        height = $("#map").height();


    var projection = d3.geo.albers()
        .center([-4.5, 54])
        .rotate([-3, 0])
        .parallels([50, 60])
        .scale(3000)
        .translate([width / 2, height / 2]);

    var path = d3.geo.path().projection(projection);

    var svg = d3.select("#map").append("svg")
        .attr("width", width)
        .attr("height", height);

    var areas = ["AB", "AL", "B", "BA", "BB", "BD", "BH", "BL", "BN", "BR", "BS", "BT", "CA", "CB", "CF", "CH", "CM", "CO", "CR", "CT", "CV", "CW", "DA", "DD", "DE", "DG", "DH", "DL", "DN", "DT", "DY", "E", "EC", "EH", "EN", "EX", "FK", "FY", "G", "GL", "GU", "HA", "HD", "HG", "HP", "HR", "HS", "HU", "HX", "IG", "IP", "IV", "KA", "KT", "KW", "KY", "L", "LA", "LD", "LE", "LL", "LN", "LS", "LU", "M", "ME", "MK", "ML", "N", "NE", "NG", "NN", "NP", "NR", "NW", "OL", "OX", "PA", "PE", "PH", "PL", "PO", "PR", "RG", "RH", "RM", "S", "SA", "SE", "SG", "SK", "SL", "SM", "SN", "SO", "SP", "SR", "SS", "ST", "SW", "SY", "TA", "TD", "TF", "TN", "TQ", "TR", "TS", "TW", "UB", "W", "WA", "WC", "WD", "WF", "WN", "WR", "WS", "WV", "YO", "ZE"];


    $.getJSON("/v1/getflu_2012_address", function (data) {
        var areadata = {};
        _.each(areas, function (a) {
            var id = a;
            var x = jQuery.grep(data, function (n, i) {
                return n.pc == id
            })
            if (x[0] != null) {
                areadata[a] = x[0].value;
            }

        });
        var color = d3.scale.quantize().range([
            "rgb(198,219,239)",
            "rgb(158,202,225)",
            "rgb(107,174,214)",
            "rgb(66,146,198)",
            "rgb(33,113,181)",
            "rgb(8,81,156)",
            "rgb(8,48,107)"]);


        color.domain(d3.extent(_.toArray(areadata)));

        d3.json("../../static/data/uk-postcode-area.json", function (error, uk) {
            svg.selectAll(".postcode_area")
                .data(topojson.feature(uk, uk.objects['uk']).features)
                .enter().append("path")
                .attr("class", "postcode_area")
                .attr("d", path)
                .style("fill", function (d) {
                    //Get data value
                    var value = areadata[d.id];

                    if (value) {
                        return color(value);
                    } else {
                        return "#AAA";
                    }
                })
                .append("svg:title")
                .attr("transform", function (d) {
                    return "translate(" + path.centroid(d) + ")";
                })
                .attr("dy", ".35em")
                .text(function (d) {
                    var value = areadata[d.id];
                    return "PC " + d.id + " Flu:" + value;
                });


            svg.append("path")
                .datum(topojson.mesh(uk, uk.objects['uk'], function (a, b) {
                    return a !== b;
                }))
                .attr("class", "mesh")
                .attr("d", path);

        });
    });


});