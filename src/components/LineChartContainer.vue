<template>
  <div class="card">
    <line-chart
      :chartdata="chartdata"
      :options="chartoptions"
      v-if="loaded"/>
    <div class="loading-card text-center" v-else>
      <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
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
      maintainAspectRatio: false,
      scales: {
        yAxes: [{
            ticks: {
                display: false
            }
        }]
      }
    }
  }),
  async mounted () {
    this.loaded = false
    try {
      let inside = this
      await this.$axios
        .get(`${process.env.VUE_APP_BACKEND_API}/predict?symbol=${this.symbol}&future_day=5`)
        .then(response => {
          inside.chartdata.datasets[0].data = Object.values(response.data['5-day result'])
          inside.chartdata.labels = Object.keys(response.data['5-day result'])
          this.loaded = true
        });
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

  .loading-card {
    margin-top: 4%;
    margin-bottom: 4%;
  }
</style>
