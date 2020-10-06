<template>
  <div class="card" >
    <table class="table" v-if="loaded">
      <thead>
        <tr>
          <th scope="col">Indicator</th>
          <th scope="col">Value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">Price Book Value</th>
          <td>{{this.stockData['ptbvAnnual']}}</td>
        </tr>
        <tr>
          <th scope="row">Current Dividen Yield</th>
          <td>{{this.stockData['currentDividendYieldTTM']}}</td>
        </tr>
        <tr>
          <th scope="row">Annual Net Debt</th>
          <td>{{this.stockData['netDebtAnnual']}}</td>
        </tr>
         <tr>
          <th scope="row">Price per Earning</th>
          <td>{{this.stockData['peNormalizedAnnual']}}</td>
        </tr>
         <tr>
          <th scope="row">Price-to-Free Cash Flow Ratio</th>
          <td>{{this.stockData['pfcfShareAnnual']}}</td>
        </tr>
      </tbody>
    </table>
    <div class="loading-card text-center" v-else>
      <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'FundamentalTable',
  props: {
    symbol: String
  },
  data() {
    return {
      loaded: false,
      stockData: [],
      errors: []
    }
  },
  async mounted() {
    this.loaded = false;
    try {
      this.getStockData();
    } catch (err) {
      this.errors << err
    }
  },
  methods: {
    getStockData: function() {
      this.$axios
      .get(`${process.env.VUE_APP_BACKEND_API}/stock_data?symbol=${this.symbol}`)
      .then(response => {
        this.stockData = response.data['metric'];
        this.loaded = true;
      }).catch( err => {
        this.errors << err
      });
    }
  }
}
</script>

<style scoped>
  .card {
    margin-top: 2%;
    margin-bottom: 2%;
    width: 75%;
  }

  .loading-card {
    margin-top: 15%;
    margin-bottom: 15%;
  }
</style>
