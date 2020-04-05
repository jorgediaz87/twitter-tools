<template>
    <b-container>
        <b-button @click="block()" block variant="danger">Block all listed accounts</b-button>
        <b-progress v-if="showProgressBar" :max="max" show-progress animated>
            <b-progress-bar
                :value="value"
                :label="`${((value / max) * 100).toFixed(2)}%`"
            ></b-progress-bar>
        </b-progress>
    </b-container>
</template>

<script>
import axios from 'axios';
const delay = (milisecs) => {
    return new Promise((resolve) => {
        setTimeout(resolve, milisecs);
    });
};

export default {
    name: 'blockAll',
    data() {
        return {
            showProgressBar: false,
            max: 20,
            value: 1,
        };
    },
    props: {
        profiles: {
            type: Array,
            default: null,
        },
    },
    methods: {
        async block() {
            this.showProgressBar = true;
            // https://stackoverflow.com/a/34349073
            for (const [index, profile] of this.profiles.entries()) {
                this.value = index + 1;
                axios
                    .post(`http://localhost:5000/api/1.0/profiles/block/${profile.id}`)
                    .then((res) => {
                        console.log(res);
                    })
                    .catch((error) => {
                        console.error(error);
                    });
                await delay(Math.floor(5000 + Math.random() * (8000 + 1 - 5000)));
            }
            this.showProgressBar = false;
        },
    },
};
</script>

<style></style>
