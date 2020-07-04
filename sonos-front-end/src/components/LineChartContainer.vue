<template>
  <div class="card" v-if="loaded">
    <line-chart
      :chartdata="chartdata"
      :options="chartoptions"/>
  </div>
</template>

<script>
import LineChart from './Chart.vue'

export default {
  name: 'LineChartContainer',
  components: { LineChart },
  props: {
    symbol: String,
  },
  data: () => ({
    loaded: false,
    chartdata: {
      labels: [],
      datasets: [
        {
          label: 'Future Prediction',
          data: []
        }
      ]
    },
    chartoptions: {
      responsive: true,
      maintainAspectRatio: false
    }
  }),
  async mounted () {
    this.loaded = false
    try {
      let inside = this
      await this.$axios
        .get(`http://localhost:8081/predict?symbol=${this.symbol}&future_day=5`)
        .then(response => {
          inside.chartdata.datasets[0].data = Object.values(response.data['5-day result'])
          inside.chartdata.labels = Object.keys(response.data['5-day result'])
        });
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>

<style scoped>
  .card {
    margin-top: 2%;
    margin-bottom: 2%;
    width: 75%;
    height: 25%;
  }
</style>
