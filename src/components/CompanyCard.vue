<template>
  <b-card :img-src="this.companyData['logo']" img-alt="Card image" img-left class="mb-3">
    <p>
      {{this.companyData['finnhubIndustry']}}
    </p>
    <h3>
      {{this.companyData['name']}}
    </h3>
  </b-card>
</template>

<script>

export default {
  name: 'CompanyCard',
  props: {
    symbol: String,
  },
    data() {
    return {
      companyData: [],
      errors: []
    }
  },
  mounted() {
    this.getCompanyData()
  },
  methods: {
    getCompanyData: function() {
      this.$axios
      .get(`${process.env.VUE_APP_ENDPOINT}/company_data?symbol=${this.symbol}`)
      .then(response => {
        this.companyData = response.data;
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

  .card-img-left {
    float: left;
    width:  100px;
    height: 100px;
    object-fit: cover;
    margin-left: 8px;
    margin-right: 8px;
    margin-top: 8px;
    margin-bottom: 8px;
  }
</style>
