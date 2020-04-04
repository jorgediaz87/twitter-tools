<template>
  <button @click="block" type="button" class="btn btn-danger">Block!</button>
</template>

<script>
import axios from "axios";

export default {
  name: "block-button",
  props: {
    profileId: {
      type: Number,
      default: null
    }
  },
  methods: {
    block() {
      const PATH = `http://localhost:5000/api/1.0/profiles/block/${this.profileId}`;
      axios
        .post(PATH)
        .then(res => {
          console.log(res);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

<style></style>
