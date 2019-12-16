<template>
  <v-row class="fill-height pt-4">
    <v-col cols="12" class="pa-0 pl-3">
      <span class="display-1 font-weight-bold">Dashboard</span>
    </v-col>
    <v-col cols="12" class="mt-4">
      <v-card class="pa-2">
        <v-card-title class="headline font-weight-bold">Bitcoin</v-card-title>
        <div id="chartdiv" class="money-graph"></div>
      </v-card>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import * as am4core from '@amcharts/amcharts4/core'
import * as am4charts from '@amcharts/amcharts4/charts'
// eslint-disable-next-line @typescript-eslint/camelcase
import am4themes_animated from '@amcharts/amcharts4/themes/animated'
// eslint-disable-next-line @typescript-eslint/camelcase
import am4themes_dark from '@amcharts/amcharts4/themes/dark'
import { Component, Vue } from 'vue-property-decorator'

am4core.useTheme(am4themes_dark)
am4core.useTheme(am4themes_animated)

@Component({})
export default class DashboardPage extends Vue {
  mounted(): void {
    const chart = am4core.create('chartdiv', am4charts.XYChart)

    const data = []
    let value = 50
    for (let i = 0; i < 300; i++) {
      const date = new Date()
      date.setHours(0, 0, 0, 0)
      date.setDate(i)
      value -= Math.round((Math.random() < 0.5 ? 1 : -1) * Math.random() * 10)
      data.push({ date: date, value: value })
    }

    chart.data = data

    // Create axes
    const dateAxis = chart.xAxes.push(new am4charts.DateAxis())
    dateAxis.renderer.minGridDistance = 60

    const valueAxis = chart.yAxes.push(new am4charts.ValueAxis())

    // Create series
    const series = chart.series.push(new am4charts.LineSeries())
    series.dataFields.valueY = 'value'
    series.dataFields.dateX = 'date'
    series.stroke = am4core.color('#617be2')
    series.strokeWidth = 3
    series.fill = am4core.color('#a7baff')
    series.fillOpacity = 0.1

    series.tooltipText = '{value}'

    if (series.tooltip) {
      series.tooltip.pointerOrientation = 'vertical'
    }

    chart.cursor = new am4charts.XYCursor()
    chart.cursor.snapToSeries = series
    chart.cursor.xAxis = dateAxis

    //chart.scrollbarY = new am4core.Scrollbar();
    // chart.scrollbarX = new am4core.Scrollbar()
    chart.scrollbarX = new am4charts.XYChartScrollbar()
    chart.scrollbarX.series.push(series)
    chart.scrollbarX.parent = chart.bottomAxesContainer
    chart.scrollbarX.background.fill = am4core.color('#424242')
    chart.scrollbarX.background.fillOpacity = 0

    // Style scrollbar
    function customizeGrip(grip: am4core.ResizeButton): void {
      // Remove default grip image
      grip.icon.disabled = true

      // Disable background
      grip.background.disabled = true

      // Add rotated rectangle as bi-di arrow
      const img = grip.createChild(am4core.Rectangle)
      img.width = 15
      img.height = 15
      img.fill = am4core.color('#617be2')
      img.rotation = 45
      img.align = 'center'
      img.valign = 'middle'

      // Add vertical bar
      const line = grip.createChild(am4core.Rectangle)
      line.height = 60
      line.width = 3
      line.fill = am4core.color('#617be2')
      line.align = 'center'
      line.valign = 'middle'
    }

    customizeGrip(chart.scrollbarX.startGrip)
    customizeGrip(chart.scrollbarX.endGrip)

    // Configure scrollbar series
    const scrollSeries = chart.scrollbarX.scrollbarChart.series.getIndex(0)
    scrollSeries.filters.clear()
    scrollSeries.fillOpacity = 0
    scrollSeries.strokeDasharray = '2,2'
  }
}
</script>

<style lang="scss" scoped>
.money-graph {
  min-height: 600px;
}
</style>
