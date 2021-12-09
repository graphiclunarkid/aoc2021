use counter::Counter;

fn increment_day(s: counter::Counter<&str>) -> counter::Counter<&str> {
    // We'll implement the logic here
    s
}

fn main() {

    // Read puzzle input from file
    let input = include_str!("day6-input");

    // Convert input into a Counter object I don't understand <Counter<_>>() yet: I just stole it
    // from https://docs.rs/counter/latest/counter/
    let school = input.trim().split(',')
        .collect::<Counter<_>>();

    println!("   Today's school: {:?}", school);

    let new_school = increment_day(school);

    println!("Tomorrow's school: {:?}", new_school);
}
