# get by month
select stat.day_month,stat.operation_type,
sum(stat.amount) as 'total' FROM formation.stat as stat
where stat.month = 2
group by stat.day_month,stat.operation_type
ORDER BY stat.day_month;

# get by year
select stat.month,stat.operation_type,
sum(stat.amount) as 'total' FROM formation.stat as stat
where stat.year = 2024
group by stat.month,stat.operation_type
ORDER BY stat.month;


