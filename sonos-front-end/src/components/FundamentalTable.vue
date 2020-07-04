<template>
  <div class="card">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Indicator</th>
          <th scope="col">Value (Ratio/Rp)</th>
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
      stockData: [],
      errors: []
    }
  },
  mounted() {
    this.getStockData()
  },
  methods: {
    getStockData: function() {
      this.$axios
      .get(`http://localhost:8081/stock_data?symbol=${this.symbol}`)
      .then(response => {
        this.stockData = response.data['metric'];
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
</style>
