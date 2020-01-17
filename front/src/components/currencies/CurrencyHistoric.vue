<template>
  <v-card>
    <v-card-text>
      <div id="chartdiv" class="money-graph"></div>
    </v-card-text>
    <v-card-actions id="interval" class="pa-0">
      <v-overflow-btn
        :items="['day', 'minute', 'hour']"
        label="Interval"
        segmented
        target="#interval"
        @change="interval => $emit('interval', interval)"
      />
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import * as am4core from '@amcharts/amcharts4/core'
import * as am4charts from '@amcharts/amcharts4/charts'
// eslint-disable-next-line @typescript-eslint/camelcase
import am4themes_animated from '@amcharts/amcharts4/themes/animated'
// eslint-disable-next-line @typescript-eslint/camelcase
import am4themes_dark from '@amcharts/amcharts4/themes/dark'
import { Component, Prop, Vue } from 'vue-property-decorator'
import { CurrencyRate } from '@/models/currency'

am4core.useTheme(am4themes_dark)
am4core.useTheme(am4themes_animated)

@Component({})
export default class CurrencyHistoric extends Vue {
  @Prop() rates: CurrencyRate[]

  chart: am4charts.XYChart = undefined

  convertRatesToChart(): any {
    return this.rates.map(rate => {
      const date = Date.parse(rate.datetime.str)
      return { date: date, value: rate.value }
    })
  }

  mounted(): void {
    this.chart = am4core.create('chartdiv', am4charts.XYChart)

    this.chart.data = this.convertRatesToChart()

    // Create axes
    const dateAxis = this.chart.xAxes.push(new am4charts.DateAxis())
    dateAxis.renderer.minGridDistance = 60

    const valueAxis = this.chart.yAxes.push(new am4charts.ValueAxis())

    // Create series
    const series = this.chart.series.push(new am4charts.LineSeries())
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

    this.chart.cursor = new am4charts.XYCursor()
    this.chart.cursor.snapToSeries = series
    this.chart.cursor.xAxis = dateAxis

    //chart.scrollbarY = new am4core.Scrollbar();
    // chart.scrollbarX = new am4core.Scrollbar()
    this.chart.scrollbarX = new am4charts.XYChartScrollbar()
    this.chart.scrollbarX.series.push(series)
    this.chart.scrollbarX.parent = this.chart.bottomAxesContainer
    this.chart.scrollbarX.background.fill = am4core.color('#424242')
    this.chart.scrollbarX.background.fillOpacity = 0

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

    customizeGrip(this.chart.scrollbarX.startGrip)
    customizeGrip(this.chart.scrollbarX.endGrip)
  }

  beforeDestroy(): void {
    this.chart.dispose()
  }
}
</script>

<style lang="scss" scoped>
.money-graph {
  min-height: 500px;
}
</style>
