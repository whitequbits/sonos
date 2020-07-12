<template>
  <div class="home">
    <div class="container mx-auto d-flex justify-content-around flex-wrap">
      <Card v-for="(stock, index) in this.$store.state.filteredStockSymbol" :key="index" v-bind:symbol="stock.symbol.slice(0, 4)" v-bind:name="stock.description"/>
    </div>
  </div>
</template>

<script>
import Card from '@/components/Card'

export default {
  name: 'StockList',
  components: {
    Card
  },
    data() {
    return {
      errors: []
    }
  },
  mounted() {
    this.getStockSymbolData()
  },
  methods: {
    getStockSymbolData: function() {
      this.$axios
      .get(`${process.env.SONOS_API_ENDPOINT}/stock_symbol`)
      .then(response => {
        this.$store.state.stockSymbol = response.data;
        this.$store.state.filteredStockSymbol = response.data;
      });
    }
  }
}
</script>
