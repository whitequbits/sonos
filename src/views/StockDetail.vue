<template>
  <div class="stock-detail">
    <div class="container">
      <CompanyCard class="mx-auto" :symbol="$route.params.symbol"/>
      <LineChartContainer class="mx-auto" :symbol="$route.params.symbol"/>
      <FundamentalTable class="mx-auto" :symbol="$route.params.symbol"/>
    </div>
  </div>
</template>

<script>
import FundamentalTable from '@/components/FundamentalTable'
import CompanyCard from '@/components/CompanyCard'
import LineChartContainer from '@/components/LineChartContainer'

export default {
  name: 'StockDetail',
  components: { 
    FundamentalTable,
    CompanyCard,
    LineChartContainer
  },
  props: {
    symbol: String
  }
}
</script>

<style scoped>
  .container {
    margin-top: 2%;
  }
</style>
