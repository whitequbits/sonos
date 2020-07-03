<template>
  <div class="home">
    <div class="container mx-auto d-flex justify-content-around flex-wrap">
      <Card v-for="(stock, index) in data" :key="index" v-bind:symbol="stock.symbol"/>
    </div>
  </div>
</template>

<script>
import Card from '@/components/Card'
import { stockData } from '@/stockData'

export default {
  name: 'Home',
  components: {
    Card
  },
  data() {
    return {
      data: [],
      errors: []
    }
  },
  mounted() {
    this.data = stockData
  }
}
</script>
